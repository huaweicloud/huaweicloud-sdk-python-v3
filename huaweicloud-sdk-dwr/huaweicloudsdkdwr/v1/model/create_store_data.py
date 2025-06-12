# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStoreData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'job_id': 'str',
        'store_name': 'str',
        'status': 'str',
        'region': 'str',
        'availability_zones': 'list[str]',
        'flavor': 'Flavor',
        'charge_info': 'ChargeInfo',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_id': 'job_id',
        'store_name': 'store_name',
        'status': 'status',
        'region': 'region',
        'availability_zones': 'availability_zones',
        'flavor': 'flavor',
        'charge_info': 'charge_info',
        'description': 'description'
    }

    def __init__(self, id=None, job_id=None, store_name=None, status=None, region=None, availability_zones=None, flavor=None, charge_info=None, description=None):
        r"""CreateStoreData

        The model defined in huaweicloud sdk

        :param id: 知识仓实例id
        :type id: str
        :param job_id: 知识仓实例创建的任务id。
        :type job_id: str
        :param store_name: 知识仓实例名称。
        :type store_name: str
        :param status: 状态。如：CREATING。
        :type status: str
        :param region: 区域ID。  取值范围：非空，请参见地区和终端节点。  取值范围：非空，请参见地区和终端节点。
        :type region: str
        :param availability_zones: 可用区ID
        :type availability_zones: list[str]
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkdwr.v1.Flavor`
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        :param description: 知识仓实例描述信息。有效长度0-255
        :type description: str
        """
        
        

        self._id = None
        self._job_id = None
        self._store_name = None
        self._status = None
        self._region = None
        self._availability_zones = None
        self._flavor = None
        self._charge_info = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.job_id = job_id
        self.store_name = store_name
        self.status = status
        if region is not None:
            self.region = region
        if availability_zones is not None:
            self.availability_zones = availability_zones
        if flavor is not None:
            self.flavor = flavor
        if charge_info is not None:
            self.charge_info = charge_info
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this CreateStoreData.

        知识仓实例id

        :return: The id of this CreateStoreData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateStoreData.

        知识仓实例id

        :param id: The id of this CreateStoreData.
        :type id: str
        """
        self._id = id

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateStoreData.

        知识仓实例创建的任务id。

        :return: The job_id of this CreateStoreData.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateStoreData.

        知识仓实例创建的任务id。

        :param job_id: The job_id of this CreateStoreData.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def store_name(self):
        r"""Gets the store_name of this CreateStoreData.

        知识仓实例名称。

        :return: The store_name of this CreateStoreData.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this CreateStoreData.

        知识仓实例名称。

        :param store_name: The store_name of this CreateStoreData.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def status(self):
        r"""Gets the status of this CreateStoreData.

        状态。如：CREATING。

        :return: The status of this CreateStoreData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateStoreData.

        状态。如：CREATING。

        :param status: The status of this CreateStoreData.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this CreateStoreData.

        区域ID。  取值范围：非空，请参见地区和终端节点。  取值范围：非空，请参见地区和终端节点。

        :return: The region of this CreateStoreData.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateStoreData.

        区域ID。  取值范围：非空，请参见地区和终端节点。  取值范围：非空，请参见地区和终端节点。

        :param region: The region of this CreateStoreData.
        :type region: str
        """
        self._region = region

    @property
    def availability_zones(self):
        r"""Gets the availability_zones of this CreateStoreData.

        可用区ID

        :return: The availability_zones of this CreateStoreData.
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        r"""Sets the availability_zones of this CreateStoreData.

        可用区ID

        :param availability_zones: The availability_zones of this CreateStoreData.
        :type availability_zones: list[str]
        """
        self._availability_zones = availability_zones

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateStoreData.

        :return: The flavor of this CreateStoreData.
        :rtype: :class:`huaweicloudsdkdwr.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateStoreData.

        :param flavor: The flavor of this CreateStoreData.
        :type flavor: :class:`huaweicloudsdkdwr.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def charge_info(self):
        r"""Gets the charge_info of this CreateStoreData.

        :return: The charge_info of this CreateStoreData.
        :rtype: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this CreateStoreData.

        :param charge_info: The charge_info of this CreateStoreData.
        :type charge_info: :class:`huaweicloudsdkdwr.v1.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def description(self):
        r"""Gets the description of this CreateStoreData.

        知识仓实例描述信息。有效长度0-255

        :return: The description of this CreateStoreData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateStoreData.

        知识仓实例描述信息。有效长度0-255

        :param description: The description of this CreateStoreData.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateStoreData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
