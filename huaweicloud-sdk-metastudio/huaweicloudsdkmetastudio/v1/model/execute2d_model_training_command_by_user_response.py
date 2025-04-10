# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Execute2dModelTrainingCommandByUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commond_result': 'str',
        'attachment_upload_url': 'list[str]',
        'multipart_data': 'list[MultipartUploadInfo]',
        'excute_failed_msg': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'commond_result': 'commond_result',
        'attachment_upload_url': 'attachment_upload_url',
        'multipart_data': 'multipart_data',
        'excute_failed_msg': 'excute_failed_msg',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, commond_result=None, attachment_upload_url=None, multipart_data=None, excute_failed_msg=None, x_request_id=None):
        r"""Execute2dModelTrainingCommandByUserResponse

        The model defined in huaweicloud sdk

        :param commond_result: 命令执行结果。 * EXCUTE_SUCCESS: 命令提交成功 * EXCUTE_FAILED: 命令提交失败
        :type commond_result: str
        :param attachment_upload_url: 附件上传地址
        :type attachment_upload_url: list[str]
        :param multipart_data: 训练视频已上传分片信息
        :type multipart_data: list[:class:`huaweicloudsdkmetastudio.v1.MultipartUploadInfo`]
        :param excute_failed_msg: 命令执行失败原因描述
        :type excute_failed_msg: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(Execute2dModelTrainingCommandByUserResponse, self).__init__()

        self._commond_result = None
        self._attachment_upload_url = None
        self._multipart_data = None
        self._excute_failed_msg = None
        self._x_request_id = None
        self.discriminator = None

        if commond_result is not None:
            self.commond_result = commond_result
        if attachment_upload_url is not None:
            self.attachment_upload_url = attachment_upload_url
        if multipart_data is not None:
            self.multipart_data = multipart_data
        if excute_failed_msg is not None:
            self.excute_failed_msg = excute_failed_msg
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def commond_result(self):
        r"""Gets the commond_result of this Execute2dModelTrainingCommandByUserResponse.

        命令执行结果。 * EXCUTE_SUCCESS: 命令提交成功 * EXCUTE_FAILED: 命令提交失败

        :return: The commond_result of this Execute2dModelTrainingCommandByUserResponse.
        :rtype: str
        """
        return self._commond_result

    @commond_result.setter
    def commond_result(self, commond_result):
        r"""Sets the commond_result of this Execute2dModelTrainingCommandByUserResponse.

        命令执行结果。 * EXCUTE_SUCCESS: 命令提交成功 * EXCUTE_FAILED: 命令提交失败

        :param commond_result: The commond_result of this Execute2dModelTrainingCommandByUserResponse.
        :type commond_result: str
        """
        self._commond_result = commond_result

    @property
    def attachment_upload_url(self):
        r"""Gets the attachment_upload_url of this Execute2dModelTrainingCommandByUserResponse.

        附件上传地址

        :return: The attachment_upload_url of this Execute2dModelTrainingCommandByUserResponse.
        :rtype: list[str]
        """
        return self._attachment_upload_url

    @attachment_upload_url.setter
    def attachment_upload_url(self, attachment_upload_url):
        r"""Sets the attachment_upload_url of this Execute2dModelTrainingCommandByUserResponse.

        附件上传地址

        :param attachment_upload_url: The attachment_upload_url of this Execute2dModelTrainingCommandByUserResponse.
        :type attachment_upload_url: list[str]
        """
        self._attachment_upload_url = attachment_upload_url

    @property
    def multipart_data(self):
        r"""Gets the multipart_data of this Execute2dModelTrainingCommandByUserResponse.

        训练视频已上传分片信息

        :return: The multipart_data of this Execute2dModelTrainingCommandByUserResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.MultipartUploadInfo`]
        """
        return self._multipart_data

    @multipart_data.setter
    def multipart_data(self, multipart_data):
        r"""Sets the multipart_data of this Execute2dModelTrainingCommandByUserResponse.

        训练视频已上传分片信息

        :param multipart_data: The multipart_data of this Execute2dModelTrainingCommandByUserResponse.
        :type multipart_data: list[:class:`huaweicloudsdkmetastudio.v1.MultipartUploadInfo`]
        """
        self._multipart_data = multipart_data

    @property
    def excute_failed_msg(self):
        r"""Gets the excute_failed_msg of this Execute2dModelTrainingCommandByUserResponse.

        命令执行失败原因描述

        :return: The excute_failed_msg of this Execute2dModelTrainingCommandByUserResponse.
        :rtype: str
        """
        return self._excute_failed_msg

    @excute_failed_msg.setter
    def excute_failed_msg(self, excute_failed_msg):
        r"""Sets the excute_failed_msg of this Execute2dModelTrainingCommandByUserResponse.

        命令执行失败原因描述

        :param excute_failed_msg: The excute_failed_msg of this Execute2dModelTrainingCommandByUserResponse.
        :type excute_failed_msg: str
        """
        self._excute_failed_msg = excute_failed_msg

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this Execute2dModelTrainingCommandByUserResponse.

        :return: The x_request_id of this Execute2dModelTrainingCommandByUserResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this Execute2dModelTrainingCommandByUserResponse.

        :param x_request_id: The x_request_id of this Execute2dModelTrainingCommandByUserResponse.
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
        if not isinstance(other, Execute2dModelTrainingCommandByUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
