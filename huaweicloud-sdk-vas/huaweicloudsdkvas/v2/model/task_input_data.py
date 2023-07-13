# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInputData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'bucket': 'str',
        'path': 'str',
        'url': 'str',
        'headers': 'object',
        'certificate_check': 'bool',
        'rtsp_path_in_response': 'str',
        'node_id': 'str',
        'device_id': 'str',
        'stream_type': 'int',
        'id': 'str'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'bucket': 'bucket',
        'path': 'path',
        'url': 'url',
        'headers': 'headers',
        'certificate_check': 'certificate_check',
        'rtsp_path_in_response': 'rtsp_path_in_response',
        'node_id': 'node_id',
        'device_id': 'device_id',
        'stream_type': 'stream_type',
        'id': 'id'
    }

    def __init__(self, stream_name=None, bucket=None, path=None, url=None, headers=None, certificate_check=None, rtsp_path_in_response=None, node_id=None, device_id=None, stream_type=None, id=None):
        """TaskInputData

        The model defined in huaweicloud sdk

        :param stream_name: VIS的视频流名称，当输入为vis类型时必填。
        :type stream_name: str
        :param bucket: OBS桶名，当输入为obs类型时必填。
        :type bucket: str
        :param path: OBS的路径，当输入为obs类型时必填。
        :type path: str
        :param url: url输入源的地址或者获取视频流地址的restful请求地址，当输入为url类型或者edgerestful类型时必填。长度不超过1000。
        :type url: str
        :param headers: 获取视频流地址的restful请求携带的请求头，当输入为edgerestful类型时可选。整体呈json格式，以键值对的形式表示请求头和取值，最多允许10组。
        :type headers: object
        :param certificate_check: 是否需要对https请求进行证书校验，当输入为edgerestful类型时必填。取值为true或者false。
        :type certificate_check: bool
        :param rtsp_path_in_response: restful请求返回的body中，视频流地址的路径，当输入为edgerestful类型时必填。长度不超过1024。
        :type rtsp_path_in_response: str
        :param node_id: IEF节点的ID，仅部分服务在输入类型为edgerestful或vcn时需填且必填。
        :type node_id: str
        :param device_id: VCN设备ID，当输入为vcn类型时必填。
        :type device_id: str
        :param stream_type: 准备进行分析的码流，当输入为vcn类型时选填。取值范围为1~3，其中1代表主码流，2代表子码流1,3代表子码流2。
        :type stream_type: int
        :param id: IEF挂载的边缘设备的ID，当输入为edgecamera类型时必填。
        :type id: str
        """
        
        

        self._stream_name = None
        self._bucket = None
        self._path = None
        self._url = None
        self._headers = None
        self._certificate_check = None
        self._rtsp_path_in_response = None
        self._node_id = None
        self._device_id = None
        self._stream_type = None
        self._id = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        if bucket is not None:
            self.bucket = bucket
        if path is not None:
            self.path = path
        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers
        if certificate_check is not None:
            self.certificate_check = certificate_check
        if rtsp_path_in_response is not None:
            self.rtsp_path_in_response = rtsp_path_in_response
        if node_id is not None:
            self.node_id = node_id
        if device_id is not None:
            self.device_id = device_id
        if stream_type is not None:
            self.stream_type = stream_type
        if id is not None:
            self.id = id

    @property
    def stream_name(self):
        """Gets the stream_name of this TaskInputData.

        VIS的视频流名称，当输入为vis类型时必填。

        :return: The stream_name of this TaskInputData.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this TaskInputData.

        VIS的视频流名称，当输入为vis类型时必填。

        :param stream_name: The stream_name of this TaskInputData.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def bucket(self):
        """Gets the bucket of this TaskInputData.

        OBS桶名，当输入为obs类型时必填。

        :return: The bucket of this TaskInputData.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this TaskInputData.

        OBS桶名，当输入为obs类型时必填。

        :param bucket: The bucket of this TaskInputData.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def path(self):
        """Gets the path of this TaskInputData.

        OBS的路径，当输入为obs类型时必填。

        :return: The path of this TaskInputData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TaskInputData.

        OBS的路径，当输入为obs类型时必填。

        :param path: The path of this TaskInputData.
        :type path: str
        """
        self._path = path

    @property
    def url(self):
        """Gets the url of this TaskInputData.

        url输入源的地址或者获取视频流地址的restful请求地址，当输入为url类型或者edgerestful类型时必填。长度不超过1000。

        :return: The url of this TaskInputData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TaskInputData.

        url输入源的地址或者获取视频流地址的restful请求地址，当输入为url类型或者edgerestful类型时必填。长度不超过1000。

        :param url: The url of this TaskInputData.
        :type url: str
        """
        self._url = url

    @property
    def headers(self):
        """Gets the headers of this TaskInputData.

        获取视频流地址的restful请求携带的请求头，当输入为edgerestful类型时可选。整体呈json格式，以键值对的形式表示请求头和取值，最多允许10组。

        :return: The headers of this TaskInputData.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this TaskInputData.

        获取视频流地址的restful请求携带的请求头，当输入为edgerestful类型时可选。整体呈json格式，以键值对的形式表示请求头和取值，最多允许10组。

        :param headers: The headers of this TaskInputData.
        :type headers: object
        """
        self._headers = headers

    @property
    def certificate_check(self):
        """Gets the certificate_check of this TaskInputData.

        是否需要对https请求进行证书校验，当输入为edgerestful类型时必填。取值为true或者false。

        :return: The certificate_check of this TaskInputData.
        :rtype: bool
        """
        return self._certificate_check

    @certificate_check.setter
    def certificate_check(self, certificate_check):
        """Sets the certificate_check of this TaskInputData.

        是否需要对https请求进行证书校验，当输入为edgerestful类型时必填。取值为true或者false。

        :param certificate_check: The certificate_check of this TaskInputData.
        :type certificate_check: bool
        """
        self._certificate_check = certificate_check

    @property
    def rtsp_path_in_response(self):
        """Gets the rtsp_path_in_response of this TaskInputData.

        restful请求返回的body中，视频流地址的路径，当输入为edgerestful类型时必填。长度不超过1024。

        :return: The rtsp_path_in_response of this TaskInputData.
        :rtype: str
        """
        return self._rtsp_path_in_response

    @rtsp_path_in_response.setter
    def rtsp_path_in_response(self, rtsp_path_in_response):
        """Sets the rtsp_path_in_response of this TaskInputData.

        restful请求返回的body中，视频流地址的路径，当输入为edgerestful类型时必填。长度不超过1024。

        :param rtsp_path_in_response: The rtsp_path_in_response of this TaskInputData.
        :type rtsp_path_in_response: str
        """
        self._rtsp_path_in_response = rtsp_path_in_response

    @property
    def node_id(self):
        """Gets the node_id of this TaskInputData.

        IEF节点的ID，仅部分服务在输入类型为edgerestful或vcn时需填且必填。

        :return: The node_id of this TaskInputData.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this TaskInputData.

        IEF节点的ID，仅部分服务在输入类型为edgerestful或vcn时需填且必填。

        :param node_id: The node_id of this TaskInputData.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def device_id(self):
        """Gets the device_id of this TaskInputData.

        VCN设备ID，当输入为vcn类型时必填。

        :return: The device_id of this TaskInputData.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this TaskInputData.

        VCN设备ID，当输入为vcn类型时必填。

        :param device_id: The device_id of this TaskInputData.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def stream_type(self):
        """Gets the stream_type of this TaskInputData.

        准备进行分析的码流，当输入为vcn类型时选填。取值范围为1~3，其中1代表主码流，2代表子码流1,3代表子码流2。

        :return: The stream_type of this TaskInputData.
        :rtype: int
        """
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type):
        """Sets the stream_type of this TaskInputData.

        准备进行分析的码流，当输入为vcn类型时选填。取值范围为1~3，其中1代表主码流，2代表子码流1,3代表子码流2。

        :param stream_type: The stream_type of this TaskInputData.
        :type stream_type: int
        """
        self._stream_type = stream_type

    @property
    def id(self):
        """Gets the id of this TaskInputData.

        IEF挂载的边缘设备的ID，当输入为edgecamera类型时必填。

        :return: The id of this TaskInputData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskInputData.

        IEF挂载的边缘设备的ID，当输入为edgecamera类型时必填。

        :param id: The id of this TaskInputData.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, TaskInputData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
