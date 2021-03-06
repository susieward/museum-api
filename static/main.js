const imgStyle = 'max-width: 100%; height: auto'

function search(){
  const keywordInput = document.querySelector('#keyword')
  const sizeInput = document.querySelector('#size')
//  const pageInput = document.querySelector('#page')
  const log = document.getElementById('log')
  const searchResults = document.getElementById('searchResults');
  if(keywordInput.value){
    let keyword = keywordInput.value;
    searchResults.innerHTML = ""
    log.textContent = "Searching..."

    let url = `/api/search/${keyword}`
    if(sizeInput.value) url = `/api/search/${keyword}/${sizeInput.value}`
    console.log('url', url)
    return fetch(url).then(res => res.json()).then(data => {
      console.log('data', data)
    //  let hasImages = data.records.filter(r => r.images.length > 0);
      if(data.records.length === 0){
        log.textContent = `No results found for "${keyword}"`
        return
      }
      let hasImages = data.records.filter(r => r.images.length > 0);
      log.textContent = `Showing results for "${keyword}" (${data.records.length})`
      let groupedByTitle = getUniqueArrayByKey(hasImages, 'title')
      console.log('groupedByTitle', groupedByTitle)
      searchResults.innerHTML = buildResultsContent(groupedByTitle)
    })
  }
}

function getImages(){
  const input = document.querySelector('input')
  const log = document.getElementById('log')
  const searchResults = document.getElementById('searchResults');
  if(input.value){
    searchResults.innerHTML = ""
    log.textContent = "Searching..."
    const url = `/api/images/${input.value}/90`
    console.log('url', url)
    return fetch(url).then(res => res.json()).then(data => {
      console.log('data', data)
      let hasImages = data.records.filter(r => r.images.length > 0);
      if(hasImages.length === 0){
        log.textContent = `No results found for "${input.value}"`
        return
      }
      log.textContent = `Showing results for "${input.value}" (${hasImages.length})`
      let groupedByTitle = getUniqueArrayByKey(hasImages, 'title')
    //  console.log('groupedByTitle', groupedByTitle)
      searchResults.innerHTML = buildResultsContent(groupedByTitle)
    })
  }
}

function getUniqueArrayByKey(arr, key){
  let uniqueValues = Array.from(new Set([...arr].map(item => item[`${key}`])))
  return uniqueValues.map(val => {
    let matches = arr.filter(item => item[`${key}`] == val);
  //  console.log('matches', matches)
    return { [`${key}`]: val, items: matches }
  })
}

function buildResultsContent(data){
  let resultsContent = `${[...data.map(result => {
    console.log('result', result)
      return `<div class="result">
          <span>Title: ${result.title}</span>
          <div class="results-container">
          ${[...result.items.map(item => {
            return getItemImages(item)
              })].join('')}
              </div>
          </div>`
          })].join('')}`
  return resultsContent
}


function getItemImages(item){
  let url =`/find/object/${item.objectid}`
  if(item.images.length > 1){
    return `
    <div>
    <span>Objectid: <a href="${url}">${item.objectid}</a></span><br>
    <span>Description: ${item.description || ''}</span><br>
    <span>Technique: ${item.technique || ''}</span><br>
    <span>Colors: ${buildColors(item) || ''}</span>
    <div class="results-container">
      ${[...item.images.map(image => {
        return `
          <img src="${image.baseimageurl}" style="${imgStyle}" />`
        })].join('')}
    </div>
    </div>`
  } else {
    return `
    <div>
    <span>Objectid: <a href="${url}">${item.objectid}</a></span><br>
    <span>Description: ${item.description || ''}</span><br>
    <span>Technique: ${item.technique || ''}</span>
      <div class="results-container">
    <img src="${item.images[0].baseimageurl}" style="${imgStyle}" />
    </div>
    </div>`
  }
}

function buildColors(item){
  console.log('item', item)
  if(!item.colors || item.colors.length === 0) return false
  return `
  <div class="colors-container">
    ${[...item.colors.map(color => {
      return `
        <div class="color">
        <span style="margin: 0 auto; border: 1px solid transparent; border-radius: 50%; width: 30px; height: 30px; background-color: ${color.color}"></span>
       <span style="font-size: 14px">${color.color}</span>
       </div>`
    })].join('')}
    </div>`
}

function openImage(result){
  let path = `https://ids.lib.harvard.edu/ids/view/${result.id}`
  location.href = path
}
