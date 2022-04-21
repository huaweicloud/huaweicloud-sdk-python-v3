# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllScalingV2PoliciesRequest:

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
        'scaling_resource_type': 'str',
        'scaling_policy_name': 'str',
        'scaling_policy_type': 'str',
        'scaling_policy_id': 'str',
        'start_number': 'int',
        'limit': 'int',
        'sort_by': 'str',
        'order': 'str',
        'enterprise_project_id': 'str',
        'alarm_id': 'str'
    }

    attribute_map = {
        'scaling_resource_id': 'scaling_resource_id',
        'scaling_resource_type': 'scaling_resource_type',
        'scaling_policy_name': 'scaling_policy_name',
        'scaling_policy_type': 'scaling_policy_type',
        'scaling_policy_id': 'scaling_policy_id',
        'start_number': 'start_number',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'order': 'order',
        'enterprise_project_id': 'enterprise_project_id',
        'alarm_id': 'alarm_id'
    }

    def __init__(self, scaling_resource_id=None, scaling_resource_type=None, scaling_policy_name=None, scaling_policy_type=None, scaling_policy_id=None, start_number=None, limit=None, sort_by=None, order=None, enterprise_project_id=None, alarm_id=None):
        """ListAllScalingV2PoliciesRequest

        The model defined in huaweicloud sdk

        :param scaling_resource_id: 伸缩组ID。
        :type scaling_resource_id: str
        :param scaling_resource_type: 伸缩资源类型：伸缩组：SCALING_GROUP；带宽：BANDWIDTH
        :type scaling_resource_type: str
        :param scaling_policy_name: 伸缩策略名称。
        :type scaling_policy_name: str
        :param scaling_policy_type: 策略类型。  告警策略：ALARM ,定时策略：SCHEDULED, 周期策略：RECURRENCE
        :type scaling_policy_type: str
        :param scaling_policy_id: 伸缩策略ID。
        :type scaling_policy_id: str
        :param start_number: 查询的起始行号，默认为0。
        :type start_number: int
        :param limit: 查询记录数，默认20，最大100。
        :type limit: int
        :param sort_by: 排序方法POLICY_NAME：根据策略名称排序;TRIGGER_CONDITION：根据触发条件排序，如升序下，告警策略最先，其余根据最近一次触发时间升序排列;CREATE_TIME：根据策略的创建时间排序。
        :type sort_by: str
        :param order: 排序顺序ASC：升序；DESC：降序
        :type order: str
        :param enterprise_project_id: 企业项目ID。  当scaling_resource_type指定为：SCALING_GROUP 传入all_granted_eps时：  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有的伸缩组对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的伸缩组对应的伸缩策略。 说明： 如果授予部分企业项目的IAM用户拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应伸缩组的伸缩策略列表。  当scaling_resource_type指定为：BANDWIDTH 传入all_granted_eps时:  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有带宽对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的带宽对应的伸缩策略，带宽在all_granted_eps场景下返回策略请参见[《EIP接口参口》查询带宽列表](https://support.huaweicloud.com/api-eip/eip_apiBandwidth_0002.html)。 不指定scaling_resource_type 当传入all_granted_eps时：  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有的伸缩组和带宽对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的伸缩组和带宽对应的伸缩策略。 说明： 如果授予部分企业项目的IAM用户拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应伸缩组的伸缩策略列表；带宽在all_granted_eps场景下返回策略请参见[《EIP接口参口》查询带宽列表](https://support.huaweicloud.com/api-eip/eip_apiBandwidth_0002.html)。
        :type enterprise_project_id: str
        :param alarm_id: 告警ID，即告警规则的ID。
        :type alarm_id: str
        """
        
        

        self._scaling_resource_id = None
        self._scaling_resource_type = None
        self._scaling_policy_name = None
        self._scaling_policy_type = None
        self._scaling_policy_id = None
        self._start_number = None
        self._limit = None
        self._sort_by = None
        self._order = None
        self._enterprise_project_id = None
        self._alarm_id = None
        self.discriminator = None

        if scaling_resource_id is not None:
            self.scaling_resource_id = scaling_resource_id
        if scaling_resource_type is not None:
            self.scaling_resource_type = scaling_resource_type
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
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if alarm_id is not None:
            self.alarm_id = alarm_id

    @property
    def scaling_resource_id(self):
        """Gets the scaling_resource_id of this ListAllScalingV2PoliciesRequest.

        伸缩组ID。

        :return: The scaling_resource_id of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_resource_id

    @scaling_resource_id.setter
    def scaling_resource_id(self, scaling_resource_id):
        """Sets the scaling_resource_id of this ListAllScalingV2PoliciesRequest.

        伸缩组ID。

        :param scaling_resource_id: The scaling_resource_id of this ListAllScalingV2PoliciesRequest.
        :type scaling_resource_id: str
        """
        self._scaling_resource_id = scaling_resource_id

    @property
    def scaling_resource_type(self):
        """Gets the scaling_resource_type of this ListAllScalingV2PoliciesRequest.

        伸缩资源类型：伸缩组：SCALING_GROUP；带宽：BANDWIDTH

        :return: The scaling_resource_type of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_resource_type

    @scaling_resource_type.setter
    def scaling_resource_type(self, scaling_resource_type):
        """Sets the scaling_resource_type of this ListAllScalingV2PoliciesRequest.

        伸缩资源类型：伸缩组：SCALING_GROUP；带宽：BANDWIDTH

        :param scaling_resource_type: The scaling_resource_type of this ListAllScalingV2PoliciesRequest.
        :type scaling_resource_type: str
        """
        self._scaling_resource_type = scaling_resource_type

    @property
    def scaling_policy_name(self):
        """Gets the scaling_policy_name of this ListAllScalingV2PoliciesRequest.

        伸缩策略名称。

        :return: The scaling_policy_name of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_name

    @scaling_policy_name.setter
    def scaling_policy_name(self, scaling_policy_name):
        """Sets the scaling_policy_name of this ListAllScalingV2PoliciesRequest.

        伸缩策略名称。

        :param scaling_policy_name: The scaling_policy_name of this ListAllScalingV2PoliciesRequest.
        :type scaling_policy_name: str
        """
        self._scaling_policy_name = scaling_policy_name

    @property
    def scaling_policy_type(self):
        """Gets the scaling_policy_type of this ListAllScalingV2PoliciesRequest.

        策略类型。  告警策略：ALARM ,定时策略：SCHEDULED, 周期策略：RECURRENCE

        :return: The scaling_policy_type of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_type

    @scaling_policy_type.setter
    def scaling_policy_type(self, scaling_policy_type):
        """Sets the scaling_policy_type of this ListAllScalingV2PoliciesRequest.

        策略类型。  告警策略：ALARM ,定时策略：SCHEDULED, 周期策略：RECURRENCE

        :param scaling_policy_type: The scaling_policy_type of this ListAllScalingV2PoliciesRequest.
        :type scaling_policy_type: str
        """
        self._scaling_policy_type = scaling_policy_type

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this ListAllScalingV2PoliciesRequest.

        伸缩策略ID。

        :return: The scaling_policy_id of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this ListAllScalingV2PoliciesRequest.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this ListAllScalingV2PoliciesRequest.
        :type scaling_policy_id: str
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def start_number(self):
        """Gets the start_number of this ListAllScalingV2PoliciesRequest.

        查询的起始行号，默认为0。

        :return: The start_number of this ListAllScalingV2PoliciesRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListAllScalingV2PoliciesRequest.

        查询的起始行号，默认为0。

        :param start_number: The start_number of this ListAllScalingV2PoliciesRequest.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListAllScalingV2PoliciesRequest.

        查询记录数，默认20，最大100。

        :return: The limit of this ListAllScalingV2PoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllScalingV2PoliciesRequest.

        查询记录数，默认20，最大100。

        :param limit: The limit of this ListAllScalingV2PoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        """Gets the sort_by of this ListAllScalingV2PoliciesRequest.

        排序方法POLICY_NAME：根据策略名称排序;TRIGGER_CONDITION：根据触发条件排序，如升序下，告警策略最先，其余根据最近一次触发时间升序排列;CREATE_TIME：根据策略的创建时间排序。

        :return: The sort_by of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListAllScalingV2PoliciesRequest.

        排序方法POLICY_NAME：根据策略名称排序;TRIGGER_CONDITION：根据触发条件排序，如升序下，告警策略最先，其余根据最近一次触发时间升序排列;CREATE_TIME：根据策略的创建时间排序。

        :param sort_by: The sort_by of this ListAllScalingV2PoliciesRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        """Gets the order of this ListAllScalingV2PoliciesRequest.

        排序顺序ASC：升序；DESC：降序

        :return: The order of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListAllScalingV2PoliciesRequest.

        排序顺序ASC：升序；DESC：降序

        :param order: The order of this ListAllScalingV2PoliciesRequest.
        :type order: str
        """
        self._order = order

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAllScalingV2PoliciesRequest.

        企业项目ID。  当scaling_resource_type指定为：SCALING_GROUP 传入all_granted_eps时：  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有的伸缩组对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的伸缩组对应的伸缩策略。 说明： 如果授予部分企业项目的IAM用户拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应伸缩组的伸缩策略列表。  当scaling_resource_type指定为：BANDWIDTH 传入all_granted_eps时:  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有带宽对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的带宽对应的伸缩策略，带宽在all_granted_eps场景下返回策略请参见[《EIP接口参口》查询带宽列表](https://support.huaweicloud.com/api-eip/eip_apiBandwidth_0002.html)。 不指定scaling_resource_type 当传入all_granted_eps时：  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有的伸缩组和带宽对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的伸缩组和带宽对应的伸缩策略。 说明： 如果授予部分企业项目的IAM用户拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应伸缩组的伸缩策略列表；带宽在all_granted_eps场景下返回策略请参见[《EIP接口参口》查询带宽列表](https://support.huaweicloud.com/api-eip/eip_apiBandwidth_0002.html)。

        :return: The enterprise_project_id of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAllScalingV2PoliciesRequest.

        企业项目ID。  当scaling_resource_type指定为：SCALING_GROUP 传入all_granted_eps时：  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有的伸缩组对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的伸缩组对应的伸缩策略。 说明： 如果授予部分企业项目的IAM用户拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应伸缩组的伸缩策略列表。  当scaling_resource_type指定为：BANDWIDTH 传入all_granted_eps时:  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有带宽对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的带宽对应的伸缩策略，带宽在all_granted_eps场景下返回策略请参见[《EIP接口参口》查询带宽列表](https://support.huaweicloud.com/api-eip/eip_apiBandwidth_0002.html)。 不指定scaling_resource_type 当传入all_granted_eps时：  华为云帐号和拥有全局权限的IAM用户可以查询该用户所有的伸缩组和带宽对应的伸缩策略。 授予部分企业项目的IAM用户，可以查询该用户所有授权企业项目下的伸缩组和带宽对应的伸缩策略。 说明： 如果授予部分企业项目的IAM用户拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应伸缩组的伸缩策略列表；带宽在all_granted_eps场景下返回策略请参见[《EIP接口参口》查询带宽列表](https://support.huaweicloud.com/api-eip/eip_apiBandwidth_0002.html)。

        :param enterprise_project_id: The enterprise_project_id of this ListAllScalingV2PoliciesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAllScalingV2PoliciesRequest.

        告警ID，即告警规则的ID。

        :return: The alarm_id of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAllScalingV2PoliciesRequest.

        告警ID，即告警规则的ID。

        :param alarm_id: The alarm_id of this ListAllScalingV2PoliciesRequest.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

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
        if not isinstance(other, ListAllScalingV2PoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
