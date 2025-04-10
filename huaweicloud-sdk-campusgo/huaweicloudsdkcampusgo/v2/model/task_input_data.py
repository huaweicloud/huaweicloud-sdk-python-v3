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
        'device_id': 'str',
        'stream_type': 'int',
        'id': 'str',
        'index': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'bucket': 'bucket',
        'path': 'path',
        'url': 'url',
        'headers': 'headers',
        'certificate_check': 'certificate_check',
        'rtsp_path_in_response': 'rtsp_path_in_response',
        'device_id': 'device_id',
        'stream_type': 'stream_type',
        'id': 'id',
        'index': 'index'
    }

    def __init__(self, stream_name=None, bucket=None, path=None, url=None, headers=None, certificate_check=None, rtsp_path_in_response=None, device_id=None, stream_type=None, id=None, index=None):
        r"""TaskInputData

        The model defined in huaweicloud sdk

        :param stream_name: VIS的视频流名称，当输入为vis类型时必选
        :type stream_name: str
        :param bucket: OBS桶名，当输入为obs类型是必选
        :type bucket: str
        :param path: OBS的路径，当输入为obs类型时必选
        :type path: str
        :param url: url输入源的地址或者获取视频流地址的restful请求地址，当输入为url或者edgerestful类型时必选
        :type url: str
        :param headers: 获取视频流的restful请求携带的请求头，当输入为edgerestful类型时可选
        :type headers: object
        :param certificate_check: 是否需要对https请求进行证书校验，当输入为edgerestful类型时必选
        :type certificate_check: bool
        :param rtsp_path_in_response: restful请求返回的body中，视频流地址的路径，当输入为edgerestful类型时必选
        :type rtsp_path_in_response: str
        :param device_id: VCN设备ID，当输入为vcn类型时必选
        :type device_id: str
        :param stream_type: 准备进行分析的码流，其中1代表主码流，2代表子码流1,3代表子码流2，当输入为vcn类型时可选
        :type stream_type: int
        :param id: IEF挂载的边缘设备的ID，当输入为edgecamera类型时必选
        :type id: str
        :param index: 可选，当前输入的序号，从0开始递增，不可重复
        :type index: int
        """
        
        

        self._stream_name = None
        self._bucket = None
        self._path = None
        self._url = None
        self._headers = None
        self._certificate_check = None
        self._rtsp_path_in_response = None
        self._device_id = None
        self._stream_type = None
        self._id = None
        self._index = None
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
        if device_id is not None:
            self.device_id = device_id
        if stream_type is not None:
            self.stream_type = stream_type
        if id is not None:
            self.id = id
        if index is not None:
            self.index = index

    @property
    def stream_name(self):
        r"""Gets the stream_name of this TaskInputData.

        VIS的视频流名称，当输入为vis类型时必选

        :return: The stream_name of this TaskInputData.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this TaskInputData.

        VIS的视频流名称，当输入为vis类型时必选

        :param stream_name: The stream_name of this TaskInputData.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def bucket(self):
        r"""Gets the bucket of this TaskInputData.

        OBS桶名，当输入为obs类型是必选

        :return: The bucket of this TaskInputData.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this TaskInputData.

        OBS桶名，当输入为obs类型是必选

        :param bucket: The bucket of this TaskInputData.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def path(self):
        r"""Gets the path of this TaskInputData.

        OBS的路径，当输入为obs类型时必选

        :return: The path of this TaskInputData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this TaskInputData.

        OBS的路径，当输入为obs类型时必选

        :param path: The path of this TaskInputData.
        :type path: str
        """
        self._path = path

    @property
    def url(self):
        r"""Gets the url of this TaskInputData.

        url输入源的地址或者获取视频流地址的restful请求地址，当输入为url或者edgerestful类型时必选

        :return: The url of this TaskInputData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this TaskInputData.

        url输入源的地址或者获取视频流地址的restful请求地址，当输入为url或者edgerestful类型时必选

        :param url: The url of this TaskInputData.
        :type url: str
        """
        self._url = url

    @property
    def headers(self):
        r"""Gets the headers of this TaskInputData.

        获取视频流的restful请求携带的请求头，当输入为edgerestful类型时可选

        :return: The headers of this TaskInputData.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this TaskInputData.

        获取视频流的restful请求携带的请求头，当输入为edgerestful类型时可选

        :param headers: The headers of this TaskInputData.
        :type headers: object
        """
        self._headers = headers

    @property
    def certificate_check(self):
        r"""Gets the certificate_check of this TaskInputData.

        是否需要对https请求进行证书校验，当输入为edgerestful类型时必选

        :return: The certificate_check of this TaskInputData.
        :rtype: bool
        """
        return self._certificate_check

    @certificate_check.setter
    def certificate_check(self, certificate_check):
        r"""Sets the certificate_check of this TaskInputData.

        是否需要对https请求进行证书校验，当输入为edgerestful类型时必选

        :param certificate_check: The certificate_check of this TaskInputData.
        :type certificate_check: bool
        """
        self._certificate_check = certificate_check

    @property
    def rtsp_path_in_response(self):
        r"""Gets the rtsp_path_in_response of this TaskInputData.

        restful请求返回的body中，视频流地址的路径，当输入为edgerestful类型时必选

        :return: The rtsp_path_in_response of this TaskInputData.
        :rtype: str
        """
        return self._rtsp_path_in_response

    @rtsp_path_in_response.setter
    def rtsp_path_in_response(self, rtsp_path_in_response):
        r"""Sets the rtsp_path_in_response of this TaskInputData.

        restful请求返回的body中，视频流地址的路径，当输入为edgerestful类型时必选

        :param rtsp_path_in_response: The rtsp_path_in_response of this TaskInputData.
        :type rtsp_path_in_response: str
        """
        self._rtsp_path_in_response = rtsp_path_in_response

    @property
    def device_id(self):
        r"""Gets the device_id of this TaskInputData.

        VCN设备ID，当输入为vcn类型时必选

        :return: The device_id of this TaskInputData.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this TaskInputData.

        VCN设备ID，当输入为vcn类型时必选

        :param device_id: The device_id of this TaskInputData.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def stream_type(self):
        r"""Gets the stream_type of this TaskInputData.

        准备进行分析的码流，其中1代表主码流，2代表子码流1,3代表子码流2，当输入为vcn类型时可选

        :return: The stream_type of this TaskInputData.
        :rtype: int
        """
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type):
        r"""Sets the stream_type of this TaskInputData.

        准备进行分析的码流，其中1代表主码流，2代表子码流1,3代表子码流2，当输入为vcn类型时可选

        :param stream_type: The stream_type of this TaskInputData.
        :type stream_type: int
        """
        self._stream_type = stream_type

    @property
    def id(self):
        r"""Gets the id of this TaskInputData.

        IEF挂载的边缘设备的ID，当输入为edgecamera类型时必选

        :return: The id of this TaskInputData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskInputData.

        IEF挂载的边缘设备的ID，当输入为edgecamera类型时必选

        :param id: The id of this TaskInputData.
        :type id: str
        """
        self._id = id

    @property
    def index(self):
        r"""Gets the index of this TaskInputData.

        可选，当前输入的序号，从0开始递增，不可重复

        :return: The index of this TaskInputData.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this TaskInputData.

        可选，当前输入的序号，从0开始递增，不可重复

        :param index: The index of this TaskInputData.
        :type index: int
        """
        self._index = index

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
