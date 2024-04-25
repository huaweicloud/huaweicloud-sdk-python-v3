# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataWareHouseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_id': 'str',
        'dw_name': 'str',
        'dw_type': 'str',
        'dw_config': 'DataWareHouseDTODwConfig'
    }

    attribute_map = {
        'dw_id': 'dw_id',
        'dw_name': 'dw_name',
        'dw_type': 'dw_type',
        'dw_config': 'dw_config'
    }

    def __init__(self, dw_id=None, dw_name=None, dw_type=None, dw_config=None):
        """DataWareHouseDTO

        The model defined in huaweicloud sdk

        :param dw_id: 数据连接ID
        :type dw_id: str
        :param dw_name: 数据连接名称
        :type dw_name: str
        :param dw_type: 数据连接类型：   * HIVE数据源   * DWS数据源   * SPARK数据源
        :type dw_type: str
        :param dw_config: 
        :type dw_config: :class:`huaweicloudsdkdataartsstudio.v1.DataWareHouseDTODwConfig`
        """
        
        

        self._dw_id = None
        self._dw_name = None
        self._dw_type = None
        self._dw_config = None
        self.discriminator = None

        if dw_id is not None:
            self.dw_id = dw_id
        if dw_name is not None:
            self.dw_name = dw_name
        if dw_type is not None:
            self.dw_type = dw_type
        if dw_config is not None:
            self.dw_config = dw_config

    @property
    def dw_id(self):
        """Gets the dw_id of this DataWareHouseDTO.

        数据连接ID

        :return: The dw_id of this DataWareHouseDTO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        """Sets the dw_id of this DataWareHouseDTO.

        数据连接ID

        :param dw_id: The dw_id of this DataWareHouseDTO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def dw_name(self):
        """Gets the dw_name of this DataWareHouseDTO.

        数据连接名称

        :return: The dw_name of this DataWareHouseDTO.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        """Sets the dw_name of this DataWareHouseDTO.

        数据连接名称

        :param dw_name: The dw_name of this DataWareHouseDTO.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def dw_type(self):
        """Gets the dw_type of this DataWareHouseDTO.

        数据连接类型：   * HIVE数据源   * DWS数据源   * SPARK数据源

        :return: The dw_type of this DataWareHouseDTO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        """Sets the dw_type of this DataWareHouseDTO.

        数据连接类型：   * HIVE数据源   * DWS数据源   * SPARK数据源

        :param dw_type: The dw_type of this DataWareHouseDTO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def dw_config(self):
        """Gets the dw_config of this DataWareHouseDTO.

        :return: The dw_config of this DataWareHouseDTO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataWareHouseDTODwConfig`
        """
        return self._dw_config

    @dw_config.setter
    def dw_config(self, dw_config):
        """Sets the dw_config of this DataWareHouseDTO.

        :param dw_config: The dw_config of this DataWareHouseDTO.
        :type dw_config: :class:`huaweicloudsdkdataartsstudio.v1.DataWareHouseDTODwConfig`
        """
        self._dw_config = dw_config

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
        if not isinstance(other, DataWareHouseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
