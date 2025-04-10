# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSysprepInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sysprep_version': 'str',
        'support_create_image': 'bool'
    }

    attribute_map = {
        'sysprep_version': 'sysprep_version',
        'support_create_image': 'support_create_image'
    }

    def __init__(self, sysprep_version=None, support_create_image=None):
        r"""ShowSysprepInfoResponse

        The model defined in huaweicloud sdk

        :param sysprep_version: sysprep版本。
        :type sysprep_version: str
        :param support_create_image: 是否支持创建镜像。
        :type support_create_image: bool
        """
        
        super(ShowSysprepInfoResponse, self).__init__()

        self._sysprep_version = None
        self._support_create_image = None
        self.discriminator = None

        if sysprep_version is not None:
            self.sysprep_version = sysprep_version
        if support_create_image is not None:
            self.support_create_image = support_create_image

    @property
    def sysprep_version(self):
        r"""Gets the sysprep_version of this ShowSysprepInfoResponse.

        sysprep版本。

        :return: The sysprep_version of this ShowSysprepInfoResponse.
        :rtype: str
        """
        return self._sysprep_version

    @sysprep_version.setter
    def sysprep_version(self, sysprep_version):
        r"""Sets the sysprep_version of this ShowSysprepInfoResponse.

        sysprep版本。

        :param sysprep_version: The sysprep_version of this ShowSysprepInfoResponse.
        :type sysprep_version: str
        """
        self._sysprep_version = sysprep_version

    @property
    def support_create_image(self):
        r"""Gets the support_create_image of this ShowSysprepInfoResponse.

        是否支持创建镜像。

        :return: The support_create_image of this ShowSysprepInfoResponse.
        :rtype: bool
        """
        return self._support_create_image

    @support_create_image.setter
    def support_create_image(self, support_create_image):
        r"""Sets the support_create_image of this ShowSysprepInfoResponse.

        是否支持创建镜像。

        :param support_create_image: The support_create_image of this ShowSysprepInfoResponse.
        :type support_create_image: bool
        """
        self._support_create_image = support_create_image

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
        if not isinstance(other, ShowSysprepInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
