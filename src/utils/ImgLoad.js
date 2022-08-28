import Image from 'next/image'

// opt-out of image optimization, no-op
const customLoader = ({ src }) => {
  return src
}

export default function Image2(props) {
  return <Image {...props} loader={customLoader} />
}