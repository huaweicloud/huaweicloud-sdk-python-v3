# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppSrcReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination_app_name': 'str',
        'destination_app_version': 'str',
        'source_app_id': 'str'
    }

    attribute_map = {
        'destination_app_name': 'destination_app_name',
        'destination_app_version': 'destination_app_version',
        'source_app_id': 'source_app_id'
    }

    def __init__(self, destination_app_name=None, destination_app_version=None, source_app_id=None):
        r"""AppSrcReq

        The model defined in huaweicloud sdk

        :param destination_app_name: 目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。
        :type destination_app_name: str
        :param destination_app_version: 目标应用版本 取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。
        :type destination_app_version: str
        :param source_app_id: 源应用id
        :type source_app_id: str
        """
        
        

        self._destination_app_name = None
        self._destination_app_version = None
        self._source_app_id = None
        self.discriminator = None

        self.destination_app_name = destination_app_name
        self.destination_app_version = destination_app_version
        self.source_app_id = source_app_id

    @property
    def destination_app_name(self):
        r"""Gets the destination_app_name of this AppSrcReq.

        目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。

        :return: The destination_app_name of this AppSrcReq.
        :rtype: str
        """
        return self._destination_app_name

    @destination_app_name.setter
    def destination_app_name(self, destination_app_name):
        r"""Sets the destination_app_name of this AppSrcReq.

        目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。

        :param destination_app_name: The destination_app_name of this AppSrcReq.
        :type destination_app_name: str
        """
        self._destination_app_name = destination_app_name

    @property
    def destination_app_version(self):
        r"""Gets the destination_app_version of this AppSrcReq.

        目标应用版本 取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。

        :return: The destination_app_version of this AppSrcReq.
        :rtype: str
        """
        return self._destination_app_version

    @destination_app_version.setter
    def destination_app_version(self, destination_app_version):
        r"""Sets the destination_app_version of this AppSrcReq.

        目标应用版本 取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。

        :param destination_app_version: The destination_app_version of this AppSrcReq.
        :type destination_app_version: str
        """
        self._destination_app_version = destination_app_version

    @property
    def source_app_id(self):
        r"""Gets the source_app_id of this AppSrcReq.

        源应用id

        :return: The source_app_id of this AppSrcReq.
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        r"""Sets the source_app_id of this AppSrcReq.

        源应用id

        :param source_app_id: The source_app_id of this AppSrcReq.
        :type source_app_id: str
        """
        self._source_app_id = source_app_id

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
        if not isinstance(other, AppSrcReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
