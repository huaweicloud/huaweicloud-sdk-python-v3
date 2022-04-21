# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePlanRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'assigned_id': 'str',
        'service_id_list': 'list[int]',
        'plan_cycle': 'PlanCycle'
    }

    attribute_map = {
        'name': 'name',
        'assigned_id': 'assigned_id',
        'service_id_list': 'service_id_list',
        'plan_cycle': 'plan_cycle'
    }

    def __init__(self, name=None, assigned_id=None, service_id_list=None, plan_cycle=None):
        """CreatePlanRequestBody

        The model defined in huaweicloud sdk

        :param name: 计划名称
        :type name: str
        :param assigned_id: 处理者id，不填时默认使用当前用户
        :type assigned_id: str
        :param service_id_list: 计划下包含的用例类型，数组长度小于10个
        :type service_id_list: list[int]
        :param plan_cycle: 
        :type plan_cycle: :class:`huaweicloudsdkcloudtest.v1.PlanCycle`
        """
        
        

        self._name = None
        self._assigned_id = None
        self._service_id_list = None
        self._plan_cycle = None
        self.discriminator = None

        self.name = name
        if assigned_id is not None:
            self.assigned_id = assigned_id
        self.service_id_list = service_id_list
        self.plan_cycle = plan_cycle

    @property
    def name(self):
        """Gets the name of this CreatePlanRequestBody.

        计划名称

        :return: The name of this CreatePlanRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePlanRequestBody.

        计划名称

        :param name: The name of this CreatePlanRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def assigned_id(self):
        """Gets the assigned_id of this CreatePlanRequestBody.

        处理者id，不填时默认使用当前用户

        :return: The assigned_id of this CreatePlanRequestBody.
        :rtype: str
        """
        return self._assigned_id

    @assigned_id.setter
    def assigned_id(self, assigned_id):
        """Sets the assigned_id of this CreatePlanRequestBody.

        处理者id，不填时默认使用当前用户

        :param assigned_id: The assigned_id of this CreatePlanRequestBody.
        :type assigned_id: str
        """
        self._assigned_id = assigned_id

    @property
    def service_id_list(self):
        """Gets the service_id_list of this CreatePlanRequestBody.

        计划下包含的用例类型，数组长度小于10个

        :return: The service_id_list of this CreatePlanRequestBody.
        :rtype: list[int]
        """
        return self._service_id_list

    @service_id_list.setter
    def service_id_list(self, service_id_list):
        """Sets the service_id_list of this CreatePlanRequestBody.

        计划下包含的用例类型，数组长度小于10个

        :param service_id_list: The service_id_list of this CreatePlanRequestBody.
        :type service_id_list: list[int]
        """
        self._service_id_list = service_id_list

    @property
    def plan_cycle(self):
        """Gets the plan_cycle of this CreatePlanRequestBody.


        :return: The plan_cycle of this CreatePlanRequestBody.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.PlanCycle`
        """
        return self._plan_cycle

    @plan_cycle.setter
    def plan_cycle(self, plan_cycle):
        """Sets the plan_cycle of this CreatePlanRequestBody.


        :param plan_cycle: The plan_cycle of this CreatePlanRequestBody.
        :type plan_cycle: :class:`huaweicloudsdkcloudtest.v1.PlanCycle`
        """
        self._plan_cycle = plan_cycle

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
        if not isinstance(other, CreatePlanRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
