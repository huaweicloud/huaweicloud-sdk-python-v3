# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFileHostEventDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'change_total_num': 'int',
        'change_file_num': 'int',
        'change_registry_num': 'int',
        'host_name': 'str',
        'data_list': 'list[FileHostEventDetailResponseInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'change_total_num': 'change_total_num',
        'change_file_num': 'change_file_num',
        'change_registry_num': 'change_registry_num',
        'host_name': 'host_name',
        'data_list': 'data_list'
    }

    def __init__(self, total_num=None, change_total_num=None, change_file_num=None, change_registry_num=None, host_name=None, data_list=None):
        r"""ListFileHostEventDetailsResponse

        The model defined in huaweicloud sdk

        :param total_num: 文件总条数
        :type total_num: int
        :param change_total_num: 变更总数
        :type change_total_num: int
        :param change_file_num: 变更文件数量
        :type change_file_num: int
        :param change_registry_num: 变更注册表数量
        :type change_registry_num: int
        :param host_name: 服务器名称
        :type host_name: str
        :param data_list: 变更文件信息列表
        :type data_list: list[:class:`huaweicloudsdkhss.v5.FileHostEventDetailResponseInfo`]
        """
        
        super(ListFileHostEventDetailsResponse, self).__init__()

        self._total_num = None
        self._change_total_num = None
        self._change_file_num = None
        self._change_registry_num = None
        self._host_name = None
        self._data_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if change_total_num is not None:
            self.change_total_num = change_total_num
        if change_file_num is not None:
            self.change_file_num = change_file_num
        if change_registry_num is not None:
            self.change_registry_num = change_registry_num
        if host_name is not None:
            self.host_name = host_name
        if data_list is not None:
            self.data_list = data_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListFileHostEventDetailsResponse.

        文件总条数

        :return: The total_num of this ListFileHostEventDetailsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListFileHostEventDetailsResponse.

        文件总条数

        :param total_num: The total_num of this ListFileHostEventDetailsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def change_total_num(self):
        r"""Gets the change_total_num of this ListFileHostEventDetailsResponse.

        变更总数

        :return: The change_total_num of this ListFileHostEventDetailsResponse.
        :rtype: int
        """
        return self._change_total_num

    @change_total_num.setter
    def change_total_num(self, change_total_num):
        r"""Sets the change_total_num of this ListFileHostEventDetailsResponse.

        变更总数

        :param change_total_num: The change_total_num of this ListFileHostEventDetailsResponse.
        :type change_total_num: int
        """
        self._change_total_num = change_total_num

    @property
    def change_file_num(self):
        r"""Gets the change_file_num of this ListFileHostEventDetailsResponse.

        变更文件数量

        :return: The change_file_num of this ListFileHostEventDetailsResponse.
        :rtype: int
        """
        return self._change_file_num

    @change_file_num.setter
    def change_file_num(self, change_file_num):
        r"""Sets the change_file_num of this ListFileHostEventDetailsResponse.

        变更文件数量

        :param change_file_num: The change_file_num of this ListFileHostEventDetailsResponse.
        :type change_file_num: int
        """
        self._change_file_num = change_file_num

    @property
    def change_registry_num(self):
        r"""Gets the change_registry_num of this ListFileHostEventDetailsResponse.

        变更注册表数量

        :return: The change_registry_num of this ListFileHostEventDetailsResponse.
        :rtype: int
        """
        return self._change_registry_num

    @change_registry_num.setter
    def change_registry_num(self, change_registry_num):
        r"""Sets the change_registry_num of this ListFileHostEventDetailsResponse.

        变更注册表数量

        :param change_registry_num: The change_registry_num of this ListFileHostEventDetailsResponse.
        :type change_registry_num: int
        """
        self._change_registry_num = change_registry_num

    @property
    def host_name(self):
        r"""Gets the host_name of this ListFileHostEventDetailsResponse.

        服务器名称

        :return: The host_name of this ListFileHostEventDetailsResponse.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListFileHostEventDetailsResponse.

        服务器名称

        :param host_name: The host_name of this ListFileHostEventDetailsResponse.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def data_list(self):
        r"""Gets the data_list of this ListFileHostEventDetailsResponse.

        变更文件信息列表

        :return: The data_list of this ListFileHostEventDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.FileHostEventDetailResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListFileHostEventDetailsResponse.

        变更文件信息列表

        :param data_list: The data_list of this ListFileHostEventDetailsResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.FileHostEventDetailResponseInfo`]
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
        if not isinstance(other, ListFileHostEventDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
