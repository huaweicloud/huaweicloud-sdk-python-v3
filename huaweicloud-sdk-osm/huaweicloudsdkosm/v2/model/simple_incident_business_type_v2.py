# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleIncidentBusinessTypeV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_type_id': 'str',
        'business_type_name': 'str',
        'case_type': 'str',
        'can_use_support_plan': 'bool'
    }

    attribute_map = {
        'business_type_id': 'business_type_id',
        'business_type_name': 'business_type_name',
        'case_type': 'case_type',
        'can_use_support_plan': 'can_use_support_plan'
    }

    def __init__(self, business_type_id=None, business_type_name=None, case_type=None, can_use_support_plan=None):
        """SimpleIncidentBusinessTypeV2

        The model defined in huaweicloud sdk

        :param business_type_id: 问题类型id
        :type business_type_id: str
        :param business_type_name: 问题类型名称
        :type business_type_name: str
        :param case_type: 对应的工单类型0咨询 5报障
        :type case_type: str
        :param can_use_support_plan: 是否可以使用支持计划
        :type can_use_support_plan: bool
        """
        
        

        self._business_type_id = None
        self._business_type_name = None
        self._case_type = None
        self._can_use_support_plan = None
        self.discriminator = None

        if business_type_id is not None:
            self.business_type_id = business_type_id
        if business_type_name is not None:
            self.business_type_name = business_type_name
        if case_type is not None:
            self.case_type = case_type
        if can_use_support_plan is not None:
            self.can_use_support_plan = can_use_support_plan

    @property
    def business_type_id(self):
        """Gets the business_type_id of this SimpleIncidentBusinessTypeV2.

        问题类型id

        :return: The business_type_id of this SimpleIncidentBusinessTypeV2.
        :rtype: str
        """
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        """Sets the business_type_id of this SimpleIncidentBusinessTypeV2.

        问题类型id

        :param business_type_id: The business_type_id of this SimpleIncidentBusinessTypeV2.
        :type business_type_id: str
        """
        self._business_type_id = business_type_id

    @property
    def business_type_name(self):
        """Gets the business_type_name of this SimpleIncidentBusinessTypeV2.

        问题类型名称

        :return: The business_type_name of this SimpleIncidentBusinessTypeV2.
        :rtype: str
        """
        return self._business_type_name

    @business_type_name.setter
    def business_type_name(self, business_type_name):
        """Sets the business_type_name of this SimpleIncidentBusinessTypeV2.

        问题类型名称

        :param business_type_name: The business_type_name of this SimpleIncidentBusinessTypeV2.
        :type business_type_name: str
        """
        self._business_type_name = business_type_name

    @property
    def case_type(self):
        """Gets the case_type of this SimpleIncidentBusinessTypeV2.

        对应的工单类型0咨询 5报障

        :return: The case_type of this SimpleIncidentBusinessTypeV2.
        :rtype: str
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        """Sets the case_type of this SimpleIncidentBusinessTypeV2.

        对应的工单类型0咨询 5报障

        :param case_type: The case_type of this SimpleIncidentBusinessTypeV2.
        :type case_type: str
        """
        self._case_type = case_type

    @property
    def can_use_support_plan(self):
        """Gets the can_use_support_plan of this SimpleIncidentBusinessTypeV2.

        是否可以使用支持计划

        :return: The can_use_support_plan of this SimpleIncidentBusinessTypeV2.
        :rtype: bool
        """
        return self._can_use_support_plan

    @can_use_support_plan.setter
    def can_use_support_plan(self, can_use_support_plan):
        """Sets the can_use_support_plan of this SimpleIncidentBusinessTypeV2.

        是否可以使用支持计划

        :param can_use_support_plan: The can_use_support_plan of this SimpleIncidentBusinessTypeV2.
        :type can_use_support_plan: bool
        """
        self._can_use_support_plan = can_use_support_plan

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
        if not isinstance(other, SimpleIncidentBusinessTypeV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
