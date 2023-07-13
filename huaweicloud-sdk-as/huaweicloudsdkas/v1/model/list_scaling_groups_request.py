# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_group_name': 'str',
        'scaling_configuration_id': 'str',
        'scaling_group_status': 'str',
        'start_number': 'int',
        'limit': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'scaling_group_name': 'scaling_group_name',
        'scaling_configuration_id': 'scaling_configuration_id',
        'scaling_group_status': 'scaling_group_status',
        'start_number': 'start_number',
        'limit': 'limit',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, scaling_group_name=None, scaling_configuration_id=None, scaling_group_status=None, start_number=None, limit=None, enterprise_project_id=None):
        """ListScalingGroupsRequest

        The model defined in huaweicloud sdk

        :param scaling_group_name: 伸缩组名称
        :type scaling_group_name: str
        :param scaling_configuration_id: 伸缩配置ID，通过查询弹性伸缩配置列表接口获取，详见[查询弹性伸缩配置列表](https://support.huaweicloud.com/api-as/as_06_0202.html)。
        :type scaling_configuration_id: str
        :param scaling_group_status: 伸缩组状态，取值如下：  - INSERVICE：正常状态 - PAUSED：停用状态 - ERROR：异常状态 - DELETING：删除中 - FREEZED：已冻结
        :type scaling_group_status: str
        :param start_number: 查询的起始行号，默认为0。最小值为0，最大值没有限制。
        :type start_number: int
        :param limit: 查询的记录条数，默认为20。取值范围为：0~100。
        :type limit: int
        :param enterprise_project_id: 企业项目ID，当传入all_granted_eps时表示查询该用户所有授权的企业项目下的伸缩组列表，如何获取企业项目ID，请参考[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)。说明：华为云帐号和拥有全局权限的IAM用户可以查询该用户所有伸缩组列表。授予部分企业项目的IAM用户，如果拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应的伸缩组列表。
        :type enterprise_project_id: str
        """
        
        

        self._scaling_group_name = None
        self._scaling_configuration_id = None
        self._scaling_group_status = None
        self._start_number = None
        self._limit = None
        self._enterprise_project_id = None
        self.discriminator = None

        if scaling_group_name is not None:
            self.scaling_group_name = scaling_group_name
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if scaling_group_status is not None:
            self.scaling_group_status = scaling_group_status
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def scaling_group_name(self):
        """Gets the scaling_group_name of this ListScalingGroupsRequest.

        伸缩组名称

        :return: The scaling_group_name of this ListScalingGroupsRequest.
        :rtype: str
        """
        return self._scaling_group_name

    @scaling_group_name.setter
    def scaling_group_name(self, scaling_group_name):
        """Sets the scaling_group_name of this ListScalingGroupsRequest.

        伸缩组名称

        :param scaling_group_name: The scaling_group_name of this ListScalingGroupsRequest.
        :type scaling_group_name: str
        """
        self._scaling_group_name = scaling_group_name

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this ListScalingGroupsRequest.

        伸缩配置ID，通过查询弹性伸缩配置列表接口获取，详见[查询弹性伸缩配置列表](https://support.huaweicloud.com/api-as/as_06_0202.html)。

        :return: The scaling_configuration_id of this ListScalingGroupsRequest.
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this ListScalingGroupsRequest.

        伸缩配置ID，通过查询弹性伸缩配置列表接口获取，详见[查询弹性伸缩配置列表](https://support.huaweicloud.com/api-as/as_06_0202.html)。

        :param scaling_configuration_id: The scaling_configuration_id of this ListScalingGroupsRequest.
        :type scaling_configuration_id: str
        """
        self._scaling_configuration_id = scaling_configuration_id

    @property
    def scaling_group_status(self):
        """Gets the scaling_group_status of this ListScalingGroupsRequest.

        伸缩组状态，取值如下：  - INSERVICE：正常状态 - PAUSED：停用状态 - ERROR：异常状态 - DELETING：删除中 - FREEZED：已冻结

        :return: The scaling_group_status of this ListScalingGroupsRequest.
        :rtype: str
        """
        return self._scaling_group_status

    @scaling_group_status.setter
    def scaling_group_status(self, scaling_group_status):
        """Sets the scaling_group_status of this ListScalingGroupsRequest.

        伸缩组状态，取值如下：  - INSERVICE：正常状态 - PAUSED：停用状态 - ERROR：异常状态 - DELETING：删除中 - FREEZED：已冻结

        :param scaling_group_status: The scaling_group_status of this ListScalingGroupsRequest.
        :type scaling_group_status: str
        """
        self._scaling_group_status = scaling_group_status

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingGroupsRequest.

        查询的起始行号，默认为0。最小值为0，最大值没有限制。

        :return: The start_number of this ListScalingGroupsRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingGroupsRequest.

        查询的起始行号，默认为0。最小值为0，最大值没有限制。

        :param start_number: The start_number of this ListScalingGroupsRequest.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingGroupsRequest.

        查询的记录条数，默认为20。取值范围为：0~100。

        :return: The limit of this ListScalingGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingGroupsRequest.

        查询的记录条数，默认为20。取值范围为：0~100。

        :param limit: The limit of this ListScalingGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListScalingGroupsRequest.

        企业项目ID，当传入all_granted_eps时表示查询该用户所有授权的企业项目下的伸缩组列表，如何获取企业项目ID，请参考[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)。说明：华为云帐号和拥有全局权限的IAM用户可以查询该用户所有伸缩组列表。授予部分企业项目的IAM用户，如果拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应的伸缩组列表。

        :return: The enterprise_project_id of this ListScalingGroupsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListScalingGroupsRequest.

        企业项目ID，当传入all_granted_eps时表示查询该用户所有授权的企业项目下的伸缩组列表，如何获取企业项目ID，请参考[查询企业项目列表](https://support.huaweicloud.com/api-em/zh-cn_topic_0121230880.html)。说明：华为云帐号和拥有全局权限的IAM用户可以查询该用户所有伸缩组列表。授予部分企业项目的IAM用户，如果拥有超过100个企业项目，则只能返回有权限的前100个企业项目对应的伸缩组列表。

        :param enterprise_project_id: The enterprise_project_id of this ListScalingGroupsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListScalingGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
