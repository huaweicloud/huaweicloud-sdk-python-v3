# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentProductCategoryV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'incident_product_category_id': 'str',
        'incident_product_category_name': 'str',
        'incident_product_category_desc': 'str',
        'incident_product_category_acronym': 'str',
        'can_use_support_plan': 'bool'
    }

    attribute_map = {
        'incident_product_category_id': 'incident_product_category_id',
        'incident_product_category_name': 'incident_product_category_name',
        'incident_product_category_desc': 'incident_product_category_desc',
        'incident_product_category_acronym': 'incident_product_category_acronym',
        'can_use_support_plan': 'can_use_support_plan'
    }

    def __init__(self, incident_product_category_id=None, incident_product_category_name=None, incident_product_category_desc=None, incident_product_category_acronym=None, can_use_support_plan=None):
        r"""IncidentProductCategoryV2

        The model defined in huaweicloud sdk

        :param incident_product_category_id: 产品类型id
        :type incident_product_category_id: str
        :param incident_product_category_name: 产品类型名称
        :type incident_product_category_name: str
        :param incident_product_category_desc: 产品类型描述
        :type incident_product_category_desc: str
        :param incident_product_category_acronym: 产品类型简称
        :type incident_product_category_acronym: str
        :param can_use_support_plan: 是否可以使用支持计划权益
        :type can_use_support_plan: bool
        """
        
        

        self._incident_product_category_id = None
        self._incident_product_category_name = None
        self._incident_product_category_desc = None
        self._incident_product_category_acronym = None
        self._can_use_support_plan = None
        self.discriminator = None

        if incident_product_category_id is not None:
            self.incident_product_category_id = incident_product_category_id
        if incident_product_category_name is not None:
            self.incident_product_category_name = incident_product_category_name
        if incident_product_category_desc is not None:
            self.incident_product_category_desc = incident_product_category_desc
        if incident_product_category_acronym is not None:
            self.incident_product_category_acronym = incident_product_category_acronym
        if can_use_support_plan is not None:
            self.can_use_support_plan = can_use_support_plan

    @property
    def incident_product_category_id(self):
        r"""Gets the incident_product_category_id of this IncidentProductCategoryV2.

        产品类型id

        :return: The incident_product_category_id of this IncidentProductCategoryV2.
        :rtype: str
        """
        return self._incident_product_category_id

    @incident_product_category_id.setter
    def incident_product_category_id(self, incident_product_category_id):
        r"""Sets the incident_product_category_id of this IncidentProductCategoryV2.

        产品类型id

        :param incident_product_category_id: The incident_product_category_id of this IncidentProductCategoryV2.
        :type incident_product_category_id: str
        """
        self._incident_product_category_id = incident_product_category_id

    @property
    def incident_product_category_name(self):
        r"""Gets the incident_product_category_name of this IncidentProductCategoryV2.

        产品类型名称

        :return: The incident_product_category_name of this IncidentProductCategoryV2.
        :rtype: str
        """
        return self._incident_product_category_name

    @incident_product_category_name.setter
    def incident_product_category_name(self, incident_product_category_name):
        r"""Sets the incident_product_category_name of this IncidentProductCategoryV2.

        产品类型名称

        :param incident_product_category_name: The incident_product_category_name of this IncidentProductCategoryV2.
        :type incident_product_category_name: str
        """
        self._incident_product_category_name = incident_product_category_name

    @property
    def incident_product_category_desc(self):
        r"""Gets the incident_product_category_desc of this IncidentProductCategoryV2.

        产品类型描述

        :return: The incident_product_category_desc of this IncidentProductCategoryV2.
        :rtype: str
        """
        return self._incident_product_category_desc

    @incident_product_category_desc.setter
    def incident_product_category_desc(self, incident_product_category_desc):
        r"""Sets the incident_product_category_desc of this IncidentProductCategoryV2.

        产品类型描述

        :param incident_product_category_desc: The incident_product_category_desc of this IncidentProductCategoryV2.
        :type incident_product_category_desc: str
        """
        self._incident_product_category_desc = incident_product_category_desc

    @property
    def incident_product_category_acronym(self):
        r"""Gets the incident_product_category_acronym of this IncidentProductCategoryV2.

        产品类型简称

        :return: The incident_product_category_acronym of this IncidentProductCategoryV2.
        :rtype: str
        """
        return self._incident_product_category_acronym

    @incident_product_category_acronym.setter
    def incident_product_category_acronym(self, incident_product_category_acronym):
        r"""Sets the incident_product_category_acronym of this IncidentProductCategoryV2.

        产品类型简称

        :param incident_product_category_acronym: The incident_product_category_acronym of this IncidentProductCategoryV2.
        :type incident_product_category_acronym: str
        """
        self._incident_product_category_acronym = incident_product_category_acronym

    @property
    def can_use_support_plan(self):
        r"""Gets the can_use_support_plan of this IncidentProductCategoryV2.

        是否可以使用支持计划权益

        :return: The can_use_support_plan of this IncidentProductCategoryV2.
        :rtype: bool
        """
        return self._can_use_support_plan

    @can_use_support_plan.setter
    def can_use_support_plan(self, can_use_support_plan):
        r"""Sets the can_use_support_plan of this IncidentProductCategoryV2.

        是否可以使用支持计划权益

        :param can_use_support_plan: The can_use_support_plan of this IncidentProductCategoryV2.
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
        if not isinstance(other, IncidentProductCategoryV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
