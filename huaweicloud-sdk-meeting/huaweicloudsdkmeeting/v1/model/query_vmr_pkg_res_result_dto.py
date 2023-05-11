# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryVmrPkgResResultDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vmr_pkg_id': 'str',
        'vmr_name': 'str',
        'vmr_pkg_parties': 'int',
        'vmr_pkg_count': 'int',
        'vmr_pkg_used_count': 'int'
    }

    attribute_map = {
        'vmr_pkg_id': 'vmrPkgId',
        'vmr_name': 'vmrName',
        'vmr_pkg_parties': 'vmrPkgParties',
        'vmr_pkg_count': 'vmrPkgCount',
        'vmr_pkg_used_count': 'vmrPkgUsedCount'
    }

    def __init__(self, vmr_pkg_id=None, vmr_name=None, vmr_pkg_parties=None, vmr_pkg_count=None, vmr_pkg_used_count=None):
        """QueryVmrPkgResResultDTO

        The model defined in huaweicloud sdk

        :param vmr_pkg_id: 云会议室套餐包id。
        :type vmr_pkg_id: str
        :param vmr_name: 云会议室套餐包名称。
        :type vmr_name: str
        :param vmr_pkg_parties: 云会议室套餐方数。
        :type vmr_pkg_parties: int
        :param vmr_pkg_count: 该云会议室套餐分配的总数。
        :type vmr_pkg_count: int
        :param vmr_pkg_used_count: 该套餐对应的云会议室已分配数量。
        :type vmr_pkg_used_count: int
        """
        
        

        self._vmr_pkg_id = None
        self._vmr_name = None
        self._vmr_pkg_parties = None
        self._vmr_pkg_count = None
        self._vmr_pkg_used_count = None
        self.discriminator = None

        if vmr_pkg_id is not None:
            self.vmr_pkg_id = vmr_pkg_id
        if vmr_name is not None:
            self.vmr_name = vmr_name
        if vmr_pkg_parties is not None:
            self.vmr_pkg_parties = vmr_pkg_parties
        if vmr_pkg_count is not None:
            self.vmr_pkg_count = vmr_pkg_count
        if vmr_pkg_used_count is not None:
            self.vmr_pkg_used_count = vmr_pkg_used_count

    @property
    def vmr_pkg_id(self):
        """Gets the vmr_pkg_id of this QueryVmrPkgResResultDTO.

        云会议室套餐包id。

        :return: The vmr_pkg_id of this QueryVmrPkgResResultDTO.
        :rtype: str
        """
        return self._vmr_pkg_id

    @vmr_pkg_id.setter
    def vmr_pkg_id(self, vmr_pkg_id):
        """Sets the vmr_pkg_id of this QueryVmrPkgResResultDTO.

        云会议室套餐包id。

        :param vmr_pkg_id: The vmr_pkg_id of this QueryVmrPkgResResultDTO.
        :type vmr_pkg_id: str
        """
        self._vmr_pkg_id = vmr_pkg_id

    @property
    def vmr_name(self):
        """Gets the vmr_name of this QueryVmrPkgResResultDTO.

        云会议室套餐包名称。

        :return: The vmr_name of this QueryVmrPkgResResultDTO.
        :rtype: str
        """
        return self._vmr_name

    @vmr_name.setter
    def vmr_name(self, vmr_name):
        """Sets the vmr_name of this QueryVmrPkgResResultDTO.

        云会议室套餐包名称。

        :param vmr_name: The vmr_name of this QueryVmrPkgResResultDTO.
        :type vmr_name: str
        """
        self._vmr_name = vmr_name

    @property
    def vmr_pkg_parties(self):
        """Gets the vmr_pkg_parties of this QueryVmrPkgResResultDTO.

        云会议室套餐方数。

        :return: The vmr_pkg_parties of this QueryVmrPkgResResultDTO.
        :rtype: int
        """
        return self._vmr_pkg_parties

    @vmr_pkg_parties.setter
    def vmr_pkg_parties(self, vmr_pkg_parties):
        """Sets the vmr_pkg_parties of this QueryVmrPkgResResultDTO.

        云会议室套餐方数。

        :param vmr_pkg_parties: The vmr_pkg_parties of this QueryVmrPkgResResultDTO.
        :type vmr_pkg_parties: int
        """
        self._vmr_pkg_parties = vmr_pkg_parties

    @property
    def vmr_pkg_count(self):
        """Gets the vmr_pkg_count of this QueryVmrPkgResResultDTO.

        该云会议室套餐分配的总数。

        :return: The vmr_pkg_count of this QueryVmrPkgResResultDTO.
        :rtype: int
        """
        return self._vmr_pkg_count

    @vmr_pkg_count.setter
    def vmr_pkg_count(self, vmr_pkg_count):
        """Sets the vmr_pkg_count of this QueryVmrPkgResResultDTO.

        该云会议室套餐分配的总数。

        :param vmr_pkg_count: The vmr_pkg_count of this QueryVmrPkgResResultDTO.
        :type vmr_pkg_count: int
        """
        self._vmr_pkg_count = vmr_pkg_count

    @property
    def vmr_pkg_used_count(self):
        """Gets the vmr_pkg_used_count of this QueryVmrPkgResResultDTO.

        该套餐对应的云会议室已分配数量。

        :return: The vmr_pkg_used_count of this QueryVmrPkgResResultDTO.
        :rtype: int
        """
        return self._vmr_pkg_used_count

    @vmr_pkg_used_count.setter
    def vmr_pkg_used_count(self, vmr_pkg_used_count):
        """Sets the vmr_pkg_used_count of this QueryVmrPkgResResultDTO.

        该套餐对应的云会议室已分配数量。

        :param vmr_pkg_used_count: The vmr_pkg_used_count of this QueryVmrPkgResResultDTO.
        :type vmr_pkg_used_count: int
        """
        self._vmr_pkg_used_count = vmr_pkg_used_count

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
        if not isinstance(other, QueryVmrPkgResResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
