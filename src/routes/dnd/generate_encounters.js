
function multiple_number_monsters(text, multiplier) {
    let split_text = text.split(/(\d+)/);
  
    let result = '';
    for (let i = 0; i < split_text.length; i++) {
      let token = split_text[i];
        
    //   might need to be careful of the -1
      if (/^\d+$/.test(token) && split_text[i-1] !== 'd') {
        let num = parseInt(token);
        let str_num = String(multiplier*num);
        let new_token = token.replace(/\d+/, str_num);
        result += new_token;
      } else {
        result += token;
      }
    }
    return result;
  }

function get_entry(table_name){
    return [["activity", "hot"], ["breach","potato"],];
}

function extract_zone_information(text) {
    let matches = text.match(/Roll on (\w+) Encounter Table and (\w+) the number of creatures. Re-roll if you get (\d+)-100\./);
    
    let multiplier = 1;
    if (matches[2] === 'double') {
      multiplier = 2;
    } else {
      multiplier = 3;
    }
  
    return [matches[1].toLowerCase(), multiplier, parseInt(matches[3])];
  }
  
  
  export function generate_encounter(zone){
    return get_entry("void")

    // let paragraph = document.createElement("p");

    // let node = document.createTextNode("<h4>Attitude to Party</h4>");
    // paragraph.appendChild(node);
    // let text = get_entry('attitude');
    // node = document.createTextNode(text);
    // paragraph.appendChild(node);


    // let element = document.getElementById(div_id);
    // element.appendChild(paragraph);
}


