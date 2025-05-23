# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'upload_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'upload_url': 'upload_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, file_id=None, upload_url=None, x_request_id=None):
        r"""CreateFileResponse

        The model defined in huaweicloud sdk

        :param file_id: 文件ID。
        :type file_id: str
        :param upload_url: 文件上传地址，有效期为24小时。 &gt; * [调用OBS的[“PUT上传”](https://support.huaweicloud.com/api-obs/obs_04_0080.html)接口上传文件。](tag:hc) &gt; * [调用OBS的[“PUT上传”](https://support.huaweicloud.com/intl/zh-cn/api-obs/obs_04_0080.html)接口上传文件。](tag:hk) &gt; * [调用OBS的“PUT上传”接口上传文件。](tag:cmcc) &gt; * 调用上述接口时，Content-MD5头必须填写，填写的值跟file_md5中的值相同，md5值获取详情请参考[使用Java代码生成文件内容的MD5值](metastudio_02_0052.xml)。 &gt; * 调用上述接口时，Content-Type头必须填写，填写的值根据不同的文件类型有所不同。     文件类型为gif，Content-Type填写image/gif     文件类型为jpeg、jpg，Content-Type填写image/jpeg     文件类型为png，Content-Type填写image/png     文件类型为mp4，Content-Type填写video/mp4     文件类型为mp3，Content-Type填写audio/mp3     文件类型为wav，Content-Type填写audio/wav     其余所有类型，Content-Type填写application/octet-stream
        :type upload_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateFileResponse, self).__init__()

        self._file_id = None
        self._upload_url = None
        self._x_request_id = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if upload_url is not None:
            self.upload_url = upload_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def file_id(self):
        r"""Gets the file_id of this CreateFileResponse.

        文件ID。

        :return: The file_id of this CreateFileResponse.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this CreateFileResponse.

        文件ID。

        :param file_id: The file_id of this CreateFileResponse.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def upload_url(self):
        r"""Gets the upload_url of this CreateFileResponse.

        文件上传地址，有效期为24小时。 > * [调用OBS的[“PUT上传”](https://support.huaweicloud.com/api-obs/obs_04_0080.html)接口上传文件。](tag:hc) > * [调用OBS的[“PUT上传”](https://support.huaweicloud.com/intl/zh-cn/api-obs/obs_04_0080.html)接口上传文件。](tag:hk) > * [调用OBS的“PUT上传”接口上传文件。](tag:cmcc) > * 调用上述接口时，Content-MD5头必须填写，填写的值跟file_md5中的值相同，md5值获取详情请参考[使用Java代码生成文件内容的MD5值](metastudio_02_0052.xml)。 > * 调用上述接口时，Content-Type头必须填写，填写的值根据不同的文件类型有所不同。     文件类型为gif，Content-Type填写image/gif     文件类型为jpeg、jpg，Content-Type填写image/jpeg     文件类型为png，Content-Type填写image/png     文件类型为mp4，Content-Type填写video/mp4     文件类型为mp3，Content-Type填写audio/mp3     文件类型为wav，Content-Type填写audio/wav     其余所有类型，Content-Type填写application/octet-stream

        :return: The upload_url of this CreateFileResponse.
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        r"""Sets the upload_url of this CreateFileResponse.

        文件上传地址，有效期为24小时。 > * [调用OBS的[“PUT上传”](https://support.huaweicloud.com/api-obs/obs_04_0080.html)接口上传文件。](tag:hc) > * [调用OBS的[“PUT上传”](https://support.huaweicloud.com/intl/zh-cn/api-obs/obs_04_0080.html)接口上传文件。](tag:hk) > * [调用OBS的“PUT上传”接口上传文件。](tag:cmcc) > * 调用上述接口时，Content-MD5头必须填写，填写的值跟file_md5中的值相同，md5值获取详情请参考[使用Java代码生成文件内容的MD5值](metastudio_02_0052.xml)。 > * 调用上述接口时，Content-Type头必须填写，填写的值根据不同的文件类型有所不同。     文件类型为gif，Content-Type填写image/gif     文件类型为jpeg、jpg，Content-Type填写image/jpeg     文件类型为png，Content-Type填写image/png     文件类型为mp4，Content-Type填写video/mp4     文件类型为mp3，Content-Type填写audio/mp3     文件类型为wav，Content-Type填写audio/wav     其余所有类型，Content-Type填写application/octet-stream

        :param upload_url: The upload_url of this CreateFileResponse.
        :type upload_url: str
        """
        self._upload_url = upload_url

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateFileResponse.

        :return: The x_request_id of this CreateFileResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateFileResponse.

        :param x_request_id: The x_request_id of this CreateFileResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
