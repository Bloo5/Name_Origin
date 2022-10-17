import React from "react";


function Result(props) {
    const {name} = props

    return (
      <div className="float-left"  style={{width:'80vw'}}>
        {name&&
          <table class="table table-bordered">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Valor</th>
                <th scope="col">Origem</th>
              </tr>
            </thead>
            <tbody>
              {
                name.map((e, index) => 
                  <tr key={index}>
                    <th scope="row">{index}</th>
                    <td>{e.value.toFixed(2)}</td>
                    <td>{e.categoria}</td>
                  </tr>
                )
              }              
            </tbody>
          </table>           
        }
      </div>

    );
  }

export default Result