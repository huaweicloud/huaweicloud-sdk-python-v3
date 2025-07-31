# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFileStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_num': 'int',
        'change_total_num': 'int',
        'change_file_num': 'int',
        'change_registry_num': 'int',
        'modify_num': 'int',
        'add_num': 'int',
        'delete_num': 'int',
        'trust_num': 'int',
        'untrust_num': 'int',
        'unknown_num': 'int'
    }

    attribute_map = {
        'host_num': 'host_num',
        'change_total_num': 'change_total_num',
        'change_file_num': 'change_file_num',
        'change_registry_num': 'change_registry_num',
        'modify_num': 'modify_num',
        'add_num': 'add_num',
        'delete_num': 'delete_num',
        'trust_num': 'trust_num',
        'untrust_num': 'untrust_num',
        'unknown_num': 'unknown_num'
    }

    def __init__(self, host_num=None, change_total_num=None, change_file_num=None, change_registry_num=None, modify_num=None, add_num=None, delete_num=None, trust_num=None, untrust_num=None, unknown_num=None):
        r"""ShowFileStatisticResponse

        The model defined in huaweicloud sdk

        :param host_num: 服务器总数
        :type host_num: int
        :param change_total_num: 总变更数
        :type change_total_num: int
        :param change_file_num: 变更文件数
        :type change_file_num: int
        :param change_registry_num: 变更注册表数量
        :type change_registry_num: int
        :param modify_num: 修改数量
        :type modify_num: int
        :param add_num: 新增数量
        :type add_num: int
        :param delete_num: 删除数量
        :type delete_num: int
        :param trust_num: trust num
        :type trust_num: int
        :param untrust_num: untrust num
        :type untrust_num: int
        :param unknown_num: unknown_num
        :type unknown_num: int
        """
        
        super(ShowFileStatisticResponse, self).__init__()

        self._host_num = None
        self._change_total_num = None
        self._change_file_num = None
        self._change_registry_num = None
        self._modify_num = None
        self._add_num = None
        self._delete_num = None
        self._trust_num = None
        self._untrust_num = None
        self._unknown_num = None
        self.discriminator = None

        if host_num is not None:
            self.host_num = host_num
        if change_total_num is not None:
            self.change_total_num = change_total_num
        if change_file_num is not None:
            self.change_file_num = change_file_num
        if change_registry_num is not None:
            self.change_registry_num = change_registry_num
        if modify_num is not None:
            self.modify_num = modify_num
        if add_num is not None:
            self.add_num = add_num
        if delete_num is not None:
            self.delete_num = delete_num
        if trust_num is not None:
            self.trust_num = trust_num
        if untrust_num is not None:
            self.untrust_num = untrust_num
        if unknown_num is not None:
            self.unknown_num = unknown_num

    @property
    def host_num(self):
        r"""Gets the host_num of this ShowFileStatisticResponse.

        服务器总数

        :return: The host_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ShowFileStatisticResponse.

        服务器总数

        :param host_num: The host_num of this ShowFileStatisticResponse.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def change_total_num(self):
        r"""Gets the change_total_num of this ShowFileStatisticResponse.

        总变更数

        :return: The change_total_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._change_total_num

    @change_total_num.setter
    def change_total_num(self, change_total_num):
        r"""Sets the change_total_num of this ShowFileStatisticResponse.

        总变更数

        :param change_total_num: The change_total_num of this ShowFileStatisticResponse.
        :type change_total_num: int
        """
        self._change_total_num = change_total_num

    @property
    def change_file_num(self):
        r"""Gets the change_file_num of this ShowFileStatisticResponse.

        变更文件数

        :return: The change_file_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._change_file_num

    @change_file_num.setter
    def change_file_num(self, change_file_num):
        r"""Sets the change_file_num of this ShowFileStatisticResponse.

        变更文件数

        :param change_file_num: The change_file_num of this ShowFileStatisticResponse.
        :type change_file_num: int
        """
        self._change_file_num = change_file_num

    @property
    def change_registry_num(self):
        r"""Gets the change_registry_num of this ShowFileStatisticResponse.

        变更注册表数量

        :return: The change_registry_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._change_registry_num

    @change_registry_num.setter
    def change_registry_num(self, change_registry_num):
        r"""Sets the change_registry_num of this ShowFileStatisticResponse.

        变更注册表数量

        :param change_registry_num: The change_registry_num of this ShowFileStatisticResponse.
        :type change_registry_num: int
        """
        self._change_registry_num = change_registry_num

    @property
    def modify_num(self):
        r"""Gets the modify_num of this ShowFileStatisticResponse.

        修改数量

        :return: The modify_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._modify_num

    @modify_num.setter
    def modify_num(self, modify_num):
        r"""Sets the modify_num of this ShowFileStatisticResponse.

        修改数量

        :param modify_num: The modify_num of this ShowFileStatisticResponse.
        :type modify_num: int
        """
        self._modify_num = modify_num

    @property
    def add_num(self):
        r"""Gets the add_num of this ShowFileStatisticResponse.

        新增数量

        :return: The add_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._add_num

    @add_num.setter
    def add_num(self, add_num):
        r"""Sets the add_num of this ShowFileStatisticResponse.

        新增数量

        :param add_num: The add_num of this ShowFileStatisticResponse.
        :type add_num: int
        """
        self._add_num = add_num

    @property
    def delete_num(self):
        r"""Gets the delete_num of this ShowFileStatisticResponse.

        删除数量

        :return: The delete_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._delete_num

    @delete_num.setter
    def delete_num(self, delete_num):
        r"""Sets the delete_num of this ShowFileStatisticResponse.

        删除数量

        :param delete_num: The delete_num of this ShowFileStatisticResponse.
        :type delete_num: int
        """
        self._delete_num = delete_num

    @property
    def trust_num(self):
        r"""Gets the trust_num of this ShowFileStatisticResponse.

        trust num

        :return: The trust_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._trust_num

    @trust_num.setter
    def trust_num(self, trust_num):
        r"""Sets the trust_num of this ShowFileStatisticResponse.

        trust num

        :param trust_num: The trust_num of this ShowFileStatisticResponse.
        :type trust_num: int
        """
        self._trust_num = trust_num

    @property
    def untrust_num(self):
        r"""Gets the untrust_num of this ShowFileStatisticResponse.

        untrust num

        :return: The untrust_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._untrust_num

    @untrust_num.setter
    def untrust_num(self, untrust_num):
        r"""Sets the untrust_num of this ShowFileStatisticResponse.

        untrust num

        :param untrust_num: The untrust_num of this ShowFileStatisticResponse.
        :type untrust_num: int
        """
        self._untrust_num = untrust_num

    @property
    def unknown_num(self):
        r"""Gets the unknown_num of this ShowFileStatisticResponse.

        unknown_num

        :return: The unknown_num of this ShowFileStatisticResponse.
        :rtype: int
        """
        return self._unknown_num

    @unknown_num.setter
    def unknown_num(self, unknown_num):
        r"""Sets the unknown_num of this ShowFileStatisticResponse.

        unknown_num

        :param unknown_num: The unknown_num of this ShowFileStatisticResponse.
        :type unknown_num: int
        """
        self._unknown_num = unknown_num

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
        if not isinstance(other, ShowFileStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
