# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingV2PoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_resource_id': 'str',
        'scaling_policy_name': 'str',
        'scaling_policy_type': 'str',
        'scaling_policy_id': 'str',
        'start_number': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'scaling_resource_id': 'scaling_resource_id',
        'scaling_policy_name': 'scaling_policy_name',
        'scaling_policy_type': 'scaling_policy_type',
        'scaling_policy_id': 'scaling_policy_id',
        'start_number': 'start_number',
        'limit': 'limit'
    }

    def __init__(self, scaling_resource_id=None, scaling_policy_name=None, scaling_policy_type=None, scaling_policy_id=None, start_number=None, limit=None):
        """ListScalingV2PoliciesRequest

        The model defined in huaweicloud sdk

        :param scaling_resource_id: 伸缩组ID。
        :type scaling_resource_id: str
        :param scaling_policy_name: 伸缩策略名称。
        :type scaling_policy_name: str
        :param scaling_policy_type: 策略类型：  - 告警策略：ALARM - 定时策略：SCHEDULED - 周期策略：RECURRENCE
        :type scaling_policy_type: str
        :param scaling_policy_id: 伸缩策略ID。
        :type scaling_policy_id: str
        :param start_number: 查询的起始行号，默认为0。
        :type start_number: int
        :param limit: 查询记录数，默认20，最大100。
        :type limit: int
        """
        
        

        self._scaling_resource_id = None
        self._scaling_policy_name = None
        self._scaling_policy_type = None
        self._scaling_policy_id = None
        self._start_number = None
        self._limit = None
        self.discriminator = None

        self.scaling_resource_id = scaling_resource_id
        if scaling_policy_name is not None:
            self.scaling_policy_name = scaling_policy_name
        if scaling_policy_type is not None:
            self.scaling_policy_type = scaling_policy_type
        if scaling_policy_id is not None:
            self.scaling_policy_id = scaling_policy_id
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit

    @property
    def scaling_resource_id(self):
        """Gets the scaling_resource_id of this ListScalingV2PoliciesRequest.

        伸缩组ID。

        :return: The scaling_resource_id of this ListScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_resource_id

    @scaling_resource_id.setter
    def scaling_resource_id(self, scaling_resource_id):
        """Sets the scaling_resource_id of this ListScalingV2PoliciesRequest.

        伸缩组ID。

        :param scaling_resource_id: The scaling_resource_id of this ListScalingV2PoliciesRequest.
        :type scaling_resource_id: str
        """
        self._scaling_resource_id = scaling_resource_id

    @property
    def scaling_policy_name(self):
        """Gets the scaling_policy_name of this ListScalingV2PoliciesRequest.

        伸缩策略名称。

        :return: The scaling_policy_name of this ListScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_name

    @scaling_policy_name.setter
    def scaling_policy_name(self, scaling_policy_name):
        """Sets the scaling_policy_name of this ListScalingV2PoliciesRequest.

        伸缩策略名称。

        :param scaling_policy_name: The scaling_policy_name of this ListScalingV2PoliciesRequest.
        :type scaling_policy_name: str
        """
        self._scaling_policy_name = scaling_policy_name

    @property
    def scaling_policy_type(self):
        """Gets the scaling_policy_type of this ListScalingV2PoliciesRequest.

        策略类型：  - 告警策略：ALARM - 定时策略：SCHEDULED - 周期策略：RECURRENCE

        :return: The scaling_policy_type of this ListScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_type

    @scaling_policy_type.setter
    def scaling_policy_type(self, scaling_policy_type):
        """Sets the scaling_policy_type of this ListScalingV2PoliciesRequest.

        策略类型：  - 告警策略：ALARM - 定时策略：SCHEDULED - 周期策略：RECURRENCE

        :param scaling_policy_type: The scaling_policy_type of this ListScalingV2PoliciesRequest.
        :type scaling_policy_type: str
        """
        self._scaling_policy_type = scaling_policy_type

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this ListScalingV2PoliciesRequest.

        伸缩策略ID。

        :return: The scaling_policy_id of this ListScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this ListScalingV2PoliciesRequest.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this ListScalingV2PoliciesRequest.
        :type scaling_policy_id: str
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingV2PoliciesRequest.

        查询的起始行号，默认为0。

        :return: The start_number of this ListScalingV2PoliciesRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingV2PoliciesRequest.

        查询的起始行号，默认为0。

        :param start_number: The start_number of this ListScalingV2PoliciesRequest.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingV2PoliciesRequest.

        查询记录数，默认20，最大100。

        :return: The limit of this ListScalingV2PoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingV2PoliciesRequest.

        查询记录数，默认20，最大100。

        :param limit: The limit of this ListScalingV2PoliciesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListScalingV2PoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
