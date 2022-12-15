# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeVulStatusRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_type': 'str',
        'data_list': 'list[VulOperateInfo]'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'data_list': 'data_list'
    }

    def __init__(self, operate_type=None, data_list=None):
        """ChangeVulStatusRequestInfo

        The model defined in huaweicloud sdk

        :param operate_type: 操作类型 - ignore : 忽略 - not_ignore : 取消忽略 - immediate_repair : 修复 - verify : 验证
        :type operate_type: str
        :param data_list: 漏洞列表
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        
        

        self._operate_type = None
        self._data_list = None
        self.discriminator = None

        if operate_type is not None:
            self.operate_type = operate_type
        if data_list is not None:
            self.data_list = data_list

    @property
    def operate_type(self):
        """Gets the operate_type of this ChangeVulStatusRequestInfo.

        操作类型 - ignore : 忽略 - not_ignore : 取消忽略 - immediate_repair : 修复 - verify : 验证

        :return: The operate_type of this ChangeVulStatusRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        """Sets the operate_type of this ChangeVulStatusRequestInfo.

        操作类型 - ignore : 忽略 - not_ignore : 取消忽略 - immediate_repair : 修复 - verify : 验证

        :param operate_type: The operate_type of this ChangeVulStatusRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def data_list(self):
        """Gets the data_list of this ChangeVulStatusRequestInfo.

        漏洞列表

        :return: The data_list of this ChangeVulStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this ChangeVulStatusRequestInfo.

        漏洞列表

        :param data_list: The data_list of this ChangeVulStatusRequestInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ChangeVulStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
