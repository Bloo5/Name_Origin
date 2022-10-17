import React, { useRef, useState } from "react";


function SearchInput(props) {
    const {getValues} = props
    const [value, setValue] = useState(null)
    const input = useRef(null)

    return (
      <div class="input-group mb-3" style={{width:'80vw'}}>
        <input ref={input} type="text" class="form-control" onChange={(e) => setValue(e.target.value)} placeholder="Escreva um sobrenome" aria-describedby="basic-addon2"/>
        <div class="input-group-append ml-3">
          <button class="btn btn-secondary" disabled={!value} type="button" onClick={(e) => getValues(value)}>Enviar</button>
        </div>
      </div>
    );
  }

export default SearchInput