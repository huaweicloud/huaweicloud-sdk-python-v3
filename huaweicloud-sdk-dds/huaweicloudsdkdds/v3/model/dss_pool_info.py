# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DssPoolInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'az_name': 'str',
        'free_capacity_gb': 'str',
        'dss_pool_volume_type': 'str',
        'dss_pool_id': 'str',
        'dss_pool_status': 'str'
    }

    attribute_map = {
        'az_name': 'az_name',
        'free_capacity_gb': 'free_capacity_gb',
        'dss_pool_volume_type': 'dss_pool_volume_type',
        'dss_pool_id': 'dss_pool_id',
        'dss_pool_status': 'dss_pool_status'
    }

    def __init__(self, az_name=None, free_capacity_gb=None, dss_pool_volume_type=None, dss_pool_id=None, dss_pool_status=None):
        """DssPoolInfo

        The model defined in huaweicloud sdk

        :param az_name: 专属存储池所在az
        :type az_name: str
        :param free_capacity_gb: 专属存储池免费空间大小，单位GB
        :type free_capacity_gb: str
        :param dss_pool_volume_type: 专属存储池磁盘类型名称，可能取值如下：  - ULTRAHIGH，表示SSD。
        :type dss_pool_volume_type: str
        :param dss_pool_id: 专属存储池ID
        :type dss_pool_id: str
        :param dss_pool_status: 专属存储池当前状态，可能取值如下： - available，表示可用。 - deploying，表示正在部署。 - enlarging，表示正在扩容。 - frozen，表示冻结。 - sellout，表示售罄。
        :type dss_pool_status: str
        """
        
        

        self._az_name = None
        self._free_capacity_gb = None
        self._dss_pool_volume_type = None
        self._dss_pool_id = None
        self._dss_pool_status = None
        self.discriminator = None

        self.az_name = az_name
        self.free_capacity_gb = free_capacity_gb
        self.dss_pool_volume_type = dss_pool_volume_type
        self.dss_pool_id = dss_pool_id
        self.dss_pool_status = dss_pool_status

    @property
    def az_name(self):
        """Gets the az_name of this DssPoolInfo.

        专属存储池所在az

        :return: The az_name of this DssPoolInfo.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        """Sets the az_name of this DssPoolInfo.

        专属存储池所在az

        :param az_name: The az_name of this DssPoolInfo.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def free_capacity_gb(self):
        """Gets the free_capacity_gb of this DssPoolInfo.

        专属存储池免费空间大小，单位GB

        :return: The free_capacity_gb of this DssPoolInfo.
        :rtype: str
        """
        return self._free_capacity_gb

    @free_capacity_gb.setter
    def free_capacity_gb(self, free_capacity_gb):
        """Sets the free_capacity_gb of this DssPoolInfo.

        专属存储池免费空间大小，单位GB

        :param free_capacity_gb: The free_capacity_gb of this DssPoolInfo.
        :type free_capacity_gb: str
        """
        self._free_capacity_gb = free_capacity_gb

    @property
    def dss_pool_volume_type(self):
        """Gets the dss_pool_volume_type of this DssPoolInfo.

        专属存储池磁盘类型名称，可能取值如下：  - ULTRAHIGH，表示SSD。

        :return: The dss_pool_volume_type of this DssPoolInfo.
        :rtype: str
        """
        return self._dss_pool_volume_type

    @dss_pool_volume_type.setter
    def dss_pool_volume_type(self, dss_pool_volume_type):
        """Sets the dss_pool_volume_type of this DssPoolInfo.

        专属存储池磁盘类型名称，可能取值如下：  - ULTRAHIGH，表示SSD。

        :param dss_pool_volume_type: The dss_pool_volume_type of this DssPoolInfo.
        :type dss_pool_volume_type: str
        """
        self._dss_pool_volume_type = dss_pool_volume_type

    @property
    def dss_pool_id(self):
        """Gets the dss_pool_id of this DssPoolInfo.

        专属存储池ID

        :return: The dss_pool_id of this DssPoolInfo.
        :rtype: str
        """
        return self._dss_pool_id

    @dss_pool_id.setter
    def dss_pool_id(self, dss_pool_id):
        """Sets the dss_pool_id of this DssPoolInfo.

        专属存储池ID

        :param dss_pool_id: The dss_pool_id of this DssPoolInfo.
        :type dss_pool_id: str
        """
        self._dss_pool_id = dss_pool_id

    @property
    def dss_pool_status(self):
        """Gets the dss_pool_status of this DssPoolInfo.

        专属存储池当前状态，可能取值如下： - available，表示可用。 - deploying，表示正在部署。 - enlarging，表示正在扩容。 - frozen，表示冻结。 - sellout，表示售罄。

        :return: The dss_pool_status of this DssPoolInfo.
        :rtype: str
        """
        return self._dss_pool_status

    @dss_pool_status.setter
    def dss_pool_status(self, dss_pool_status):
        """Sets the dss_pool_status of this DssPoolInfo.

        专属存储池当前状态，可能取值如下： - available，表示可用。 - deploying，表示正在部署。 - enlarging，表示正在扩容。 - frozen，表示冻结。 - sellout，表示售罄。

        :param dss_pool_status: The dss_pool_status of this DssPoolInfo.
        :type dss_pool_status: str
        """
        self._dss_pool_status = dss_pool_status

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
        if not isinstance(other, DssPoolInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
