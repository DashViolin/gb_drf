import React from 'react';


class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.handleFilterTextChange = this.handleFilterTextChange.bind(this);
  }

  handleFilterTextChange(event) {
    this.props.onFilterTextChange(event.target.value);
  }

  render() {
    return (
      <div className="container">
        <form>
          <input type="text" placeholder="Search..." value={this.props.filterText} onChange={this.handleFilterTextChange} />
        </form>
      </div>
    );
  }
}

export default SearchBar
