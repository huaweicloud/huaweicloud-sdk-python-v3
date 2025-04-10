# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceEngineDistributionListEngineDistribution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'total': 'int',
        'instance_infos': 'list[InstanceEngineDistributionListInstanceInfos]'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'total': 'total',
        'instance_infos': 'instance_infos'
    }

    def __init__(self, datastore_type=None, total=None, instance_infos=None):
        r"""InstanceEngineDistributionListEngineDistribution

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param total: 总数
        :type total: int
        :param instance_infos: 实例信息
        :type instance_infos: list[:class:`huaweicloudsdkdas.v3.InstanceEngineDistributionListInstanceInfos`]
        """
        
        

        self._datastore_type = None
        self._total = None
        self._instance_infos = None
        self.discriminator = None

        if datastore_type is not None:
            self.datastore_type = datastore_type
        if total is not None:
            self.total = total
        if instance_infos is not None:
            self.instance_infos = instance_infos

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this InstanceEngineDistributionListEngineDistribution.

        数据库类型

        :return: The datastore_type of this InstanceEngineDistributionListEngineDistribution.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this InstanceEngineDistributionListEngineDistribution.

        数据库类型

        :param datastore_type: The datastore_type of this InstanceEngineDistributionListEngineDistribution.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def total(self):
        r"""Gets the total of this InstanceEngineDistributionListEngineDistribution.

        总数

        :return: The total of this InstanceEngineDistributionListEngineDistribution.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this InstanceEngineDistributionListEngineDistribution.

        总数

        :param total: The total of this InstanceEngineDistributionListEngineDistribution.
        :type total: int
        """
        self._total = total

    @property
    def instance_infos(self):
        r"""Gets the instance_infos of this InstanceEngineDistributionListEngineDistribution.

        实例信息

        :return: The instance_infos of this InstanceEngineDistributionListEngineDistribution.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InstanceEngineDistributionListInstanceInfos`]
        """
        return self._instance_infos

    @instance_infos.setter
    def instance_infos(self, instance_infos):
        r"""Sets the instance_infos of this InstanceEngineDistributionListEngineDistribution.

        实例信息

        :param instance_infos: The instance_infos of this InstanceEngineDistributionListEngineDistribution.
        :type instance_infos: list[:class:`huaweicloudsdkdas.v3.InstanceEngineDistributionListInstanceInfos`]
        """
        self._instance_infos = instance_infos

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
        if not isinstance(other, InstanceEngineDistributionListEngineDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
