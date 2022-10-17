import axios from "axios";
import React, { useEffect, useState } from "react";
import Result from "../components/result";
import SearchInput from "../components/searchInput";


function NameSearchPage() {

    const [name, setName ] = useState(null)

    const getValues = async (val) => {
        axios.get(`http://127.0.0.1:5000/model/${val}`).then(response => {
            setName(response.data)
        }).catch(error => {
            console.log(error)
        })
    }

    return (
        <>
            <SearchInput getValues={val => getValues(val)}/>
            <Result name={name}/>
        </>
    );
  }

export default NameSearchPage