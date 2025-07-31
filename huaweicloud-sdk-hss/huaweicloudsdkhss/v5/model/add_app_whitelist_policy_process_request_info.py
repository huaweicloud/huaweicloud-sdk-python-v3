# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddAppWhitelistPolicyProcessRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_info_list': 'list[AddAppWhitelistPolicyProcessInfo]'
    }

    attribute_map = {
        'process_info_list': 'process_info_list'
    }

    def __init__(self, process_info_list=None):
        r"""AddAppWhitelistPolicyProcessRequestInfo

        The model defined in huaweicloud sdk

        :param process_info_list: 白名单进程列表
        :type process_info_list: list[:class:`huaweicloudsdkhss.v5.AddAppWhitelistPolicyProcessInfo`]
        """
        
        

        self._process_info_list = None
        self.discriminator = None

        self.process_info_list = process_info_list

    @property
    def process_info_list(self):
        r"""Gets the process_info_list of this AddAppWhitelistPolicyProcessRequestInfo.

        白名单进程列表

        :return: The process_info_list of this AddAppWhitelistPolicyProcessRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AddAppWhitelistPolicyProcessInfo`]
        """
        return self._process_info_list

    @process_info_list.setter
    def process_info_list(self, process_info_list):
        r"""Sets the process_info_list of this AddAppWhitelistPolicyProcessRequestInfo.

        白名单进程列表

        :param process_info_list: The process_info_list of this AddAppWhitelistPolicyProcessRequestInfo.
        :type process_info_list: list[:class:`huaweicloudsdkhss.v5.AddAppWhitelistPolicyProcessInfo`]
        """
        self._process_info_list = process_info_list

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
        if not isinstance(other, AddAppWhitelistPolicyProcessRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
