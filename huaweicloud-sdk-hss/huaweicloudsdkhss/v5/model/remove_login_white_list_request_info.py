# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveLoginWhiteListRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_list': 'list[LoginWhiteListRequestInfo]',
        'delete_all': 'bool'
    }

    attribute_map = {
        'data_list': 'data_list',
        'delete_all': 'delete_all'
    }

    def __init__(self, data_list=None, delete_all=None):
        r"""RemoveLoginWhiteListRequestInfo

        The model defined in huaweicloud sdk

        :param data_list: 删除登录白名单详情
        :type data_list: list[:class:`huaweicloudsdkhss.v5.LoginWhiteListRequestInfo`]
        :param delete_all: 是否删除所有白名单内容
        :type delete_all: bool
        """
        
        

        self._data_list = None
        self._delete_all = None
        self.discriminator = None

        if data_list is not None:
            self.data_list = data_list
        if delete_all is not None:
            self.delete_all = delete_all

    @property
    def data_list(self):
        r"""Gets the data_list of this RemoveLoginWhiteListRequestInfo.

        删除登录白名单详情

        :return: The data_list of this RemoveLoginWhiteListRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.LoginWhiteListRequestInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this RemoveLoginWhiteListRequestInfo.

        删除登录白名单详情

        :param data_list: The data_list of this RemoveLoginWhiteListRequestInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.LoginWhiteListRequestInfo`]
        """
        self._data_list = data_list

    @property
    def delete_all(self):
        r"""Gets the delete_all of this RemoveLoginWhiteListRequestInfo.

        是否删除所有白名单内容

        :return: The delete_all of this RemoveLoginWhiteListRequestInfo.
        :rtype: bool
        """
        return self._delete_all

    @delete_all.setter
    def delete_all(self, delete_all):
        r"""Sets the delete_all of this RemoveLoginWhiteListRequestInfo.

        是否删除所有白名单内容

        :param delete_all: The delete_all of this RemoveLoginWhiteListRequestInfo.
        :type delete_all: bool
        """
        self._delete_all = delete_all

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
        if not isinstance(other, RemoveLoginWhiteListRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
