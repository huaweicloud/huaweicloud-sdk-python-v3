# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'path': 'str',
        'url': 'str',
        'id': 'str',
        'stream_name': 'str',
        'node_id': 'str',
        'certificate_check': 'bool',
        'rtsp_path_in_response': 'str',
        'device_id': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'path': 'path',
        'url': 'url',
        'id': 'id',
        'stream_name': 'stream_name',
        'node_id': 'node_id',
        'certificate_check': 'certificate_check',
        'rtsp_path_in_response': 'rtsp_path_in_response',
        'device_id': 'device_id'
    }

    def __init__(self, bucket=None, path=None, url=None, id=None, stream_name=None, node_id=None, certificate_check=None, rtsp_path_in_response=None, device_id=None):
        """InputData

        The model defined in huaweicloud sdk

        :param bucket: type为obs时输入参数  OBS桶名称。 
        :type bucket: str
        :param path: type为obs时输入参数  OBS桶内的路径，例如“output/c1.mp4”。 
        :type path: str
        :param url: type为url或edgerestful时输入参数  type为url时表示视频数据的URL，目前支持OBS URL，且需要设置该URL对匿名用户可读权限。 type为edgerestful时表示容器获取EDGERESTFUL流的rest请求。格式：http(s):ip:port/xxx。 
        :type url: str
        :param id: type为edgecamera时输入参数  边缘摄像头id。 
        :type id: str
        :param stream_name: type为vis时输入参数  视频接入服务中的视频流名称。 
        :type stream_name: str
        :param node_id: type为edgerestful或vcn时输入参数  用于运行的边缘节点id, 下发边缘多任务作业时该字段不填写。 
        :type node_id: str
        :param certificate_check: type为edgerestful时输入参数  true：算法侧需要对https请求进行证书校验。 false：算法侧无需证书校验。 默认值：false。 平台侧仅对齐进行输入校验，不涉及业务逻辑。 
        :type certificate_check: bool
        :param rtsp_path_in_response: type为edgerestful时输入参数  返回body体中edgerestful流地址的路径，不能以/开头。例如：data/url。 
        :type rtsp_path_in_response: str
        :param device_id: type为vcn时输入参数  设备id号，符合正则表达式：^([0-9]{20}[#]{1}[a-zA-Z0-9]{32})|([0-9]{20}[#]{1}[0-9]{1,10}[#]{1}[a-zA-Z0-9]{32})$。 
        :type device_id: str
        """
        
        

        self._bucket = None
        self._path = None
        self._url = None
        self._id = None
        self._stream_name = None
        self._node_id = None
        self._certificate_check = None
        self._rtsp_path_in_response = None
        self._device_id = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if path is not None:
            self.path = path
        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if stream_name is not None:
            self.stream_name = stream_name
        if node_id is not None:
            self.node_id = node_id
        if certificate_check is not None:
            self.certificate_check = certificate_check
        if rtsp_path_in_response is not None:
            self.rtsp_path_in_response = rtsp_path_in_response
        if device_id is not None:
            self.device_id = device_id

    @property
    def bucket(self):
        """Gets the bucket of this InputData.

        type为obs时输入参数  OBS桶名称。 

        :return: The bucket of this InputData.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this InputData.

        type为obs时输入参数  OBS桶名称。 

        :param bucket: The bucket of this InputData.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def path(self):
        """Gets the path of this InputData.

        type为obs时输入参数  OBS桶内的路径，例如“output/c1.mp4”。 

        :return: The path of this InputData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this InputData.

        type为obs时输入参数  OBS桶内的路径，例如“output/c1.mp4”。 

        :param path: The path of this InputData.
        :type path: str
        """
        self._path = path

    @property
    def url(self):
        """Gets the url of this InputData.

        type为url或edgerestful时输入参数  type为url时表示视频数据的URL，目前支持OBS URL，且需要设置该URL对匿名用户可读权限。 type为edgerestful时表示容器获取EDGERESTFUL流的rest请求。格式：http(s):ip:port/xxx。 

        :return: The url of this InputData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InputData.

        type为url或edgerestful时输入参数  type为url时表示视频数据的URL，目前支持OBS URL，且需要设置该URL对匿名用户可读权限。 type为edgerestful时表示容器获取EDGERESTFUL流的rest请求。格式：http(s):ip:port/xxx。 

        :param url: The url of this InputData.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        """Gets the id of this InputData.

        type为edgecamera时输入参数  边缘摄像头id。 

        :return: The id of this InputData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InputData.

        type为edgecamera时输入参数  边缘摄像头id。 

        :param id: The id of this InputData.
        :type id: str
        """
        self._id = id

    @property
    def stream_name(self):
        """Gets the stream_name of this InputData.

        type为vis时输入参数  视频接入服务中的视频流名称。 

        :return: The stream_name of this InputData.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this InputData.

        type为vis时输入参数  视频接入服务中的视频流名称。 

        :param stream_name: The stream_name of this InputData.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def node_id(self):
        """Gets the node_id of this InputData.

        type为edgerestful或vcn时输入参数  用于运行的边缘节点id, 下发边缘多任务作业时该字段不填写。 

        :return: The node_id of this InputData.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this InputData.

        type为edgerestful或vcn时输入参数  用于运行的边缘节点id, 下发边缘多任务作业时该字段不填写。 

        :param node_id: The node_id of this InputData.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def certificate_check(self):
        """Gets the certificate_check of this InputData.

        type为edgerestful时输入参数  true：算法侧需要对https请求进行证书校验。 false：算法侧无需证书校验。 默认值：false。 平台侧仅对齐进行输入校验，不涉及业务逻辑。 

        :return: The certificate_check of this InputData.
        :rtype: bool
        """
        return self._certificate_check

    @certificate_check.setter
    def certificate_check(self, certificate_check):
        """Sets the certificate_check of this InputData.

        type为edgerestful时输入参数  true：算法侧需要对https请求进行证书校验。 false：算法侧无需证书校验。 默认值：false。 平台侧仅对齐进行输入校验，不涉及业务逻辑。 

        :param certificate_check: The certificate_check of this InputData.
        :type certificate_check: bool
        """
        self._certificate_check = certificate_check

    @property
    def rtsp_path_in_response(self):
        """Gets the rtsp_path_in_response of this InputData.

        type为edgerestful时输入参数  返回body体中edgerestful流地址的路径，不能以/开头。例如：data/url。 

        :return: The rtsp_path_in_response of this InputData.
        :rtype: str
        """
        return self._rtsp_path_in_response

    @rtsp_path_in_response.setter
    def rtsp_path_in_response(self, rtsp_path_in_response):
        """Sets the rtsp_path_in_response of this InputData.

        type为edgerestful时输入参数  返回body体中edgerestful流地址的路径，不能以/开头。例如：data/url。 

        :param rtsp_path_in_response: The rtsp_path_in_response of this InputData.
        :type rtsp_path_in_response: str
        """
        self._rtsp_path_in_response = rtsp_path_in_response

    @property
    def device_id(self):
        """Gets the device_id of this InputData.

        type为vcn时输入参数  设备id号，符合正则表达式：^([0-9]{20}[#]{1}[a-zA-Z0-9]{32})|([0-9]{20}[#]{1}[0-9]{1,10}[#]{1}[a-zA-Z0-9]{32})$。 

        :return: The device_id of this InputData.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this InputData.

        type为vcn时输入参数  设备id号，符合正则表达式：^([0-9]{20}[#]{1}[a-zA-Z0-9]{32})|([0-9]{20}[#]{1}[0-9]{1,10}[#]{1}[a-zA-Z0-9]{32})$。 

        :param device_id: The device_id of this InputData.
        :type device_id: str
        """
        self._device_id = device_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InputData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
