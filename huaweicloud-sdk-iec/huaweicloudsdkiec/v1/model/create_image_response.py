# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'image_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'image_id': 'image_id'
    }

    def __init__(self, job_id=None, image_id=None):
        """CreateImageResponse

        The model defined in huaweicloud sdk

        :param job_id: 提交任务成功后返回的任务ID，用户可以使用该ID对任务执行情况进行查询。
        :type job_id: str
        :param image_id: 创建镜像的ID。
        :type image_id: str
        """
        
        super(CreateImageResponse, self).__init__()

        self._job_id = None
        self._image_id = None
        self.discriminator = None

        self.job_id = job_id
        if image_id is not None:
            self.image_id = image_id

    @property
    def job_id(self):
        """Gets the job_id of this CreateImageResponse.

        提交任务成功后返回的任务ID，用户可以使用该ID对任务执行情况进行查询。

        :return: The job_id of this CreateImageResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateImageResponse.

        提交任务成功后返回的任务ID，用户可以使用该ID对任务执行情况进行查询。

        :param job_id: The job_id of this CreateImageResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def image_id(self):
        """Gets the image_id of this CreateImageResponse.

        创建镜像的ID。

        :return: The image_id of this CreateImageResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateImageResponse.

        创建镜像的ID。

        :param image_id: The image_id of this CreateImageResponse.
        :type image_id: str
        """
        self._image_id = image_id

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
        if not isinstance(other, CreateImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
