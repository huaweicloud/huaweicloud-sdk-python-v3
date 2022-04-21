# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentSubTypeV2Do:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'incident_sub_type_id': 'str',
        'incident_sub_type_name': 'str',
        'incident_product_category_list': 'list[IncidentProductCategoryV2]'
    }

    attribute_map = {
        'incident_sub_type_id': 'incident_sub_type_id',
        'incident_sub_type_name': 'incident_sub_type_name',
        'incident_product_category_list': 'incident_product_category_list'
    }

    def __init__(self, incident_sub_type_id=None, incident_sub_type_name=None, incident_product_category_list=None):
        """IncidentSubTypeV2Do

        The model defined in huaweicloud sdk

        :param incident_sub_type_id: 工单子类型id
        :type incident_sub_type_id: str
        :param incident_sub_type_name: 工单子类型名称
        :type incident_sub_type_name: str
        :param incident_product_category_list: 产品类型列表
        :type incident_product_category_list: list[:class:`huaweicloudsdkosm.v2.IncidentProductCategoryV2`]
        """
        
        

        self._incident_sub_type_id = None
        self._incident_sub_type_name = None
        self._incident_product_category_list = None
        self.discriminator = None

        if incident_sub_type_id is not None:
            self.incident_sub_type_id = incident_sub_type_id
        if incident_sub_type_name is not None:
            self.incident_sub_type_name = incident_sub_type_name
        if incident_product_category_list is not None:
            self.incident_product_category_list = incident_product_category_list

    @property
    def incident_sub_type_id(self):
        """Gets the incident_sub_type_id of this IncidentSubTypeV2Do.

        工单子类型id

        :return: The incident_sub_type_id of this IncidentSubTypeV2Do.
        :rtype: str
        """
        return self._incident_sub_type_id

    @incident_sub_type_id.setter
    def incident_sub_type_id(self, incident_sub_type_id):
        """Sets the incident_sub_type_id of this IncidentSubTypeV2Do.

        工单子类型id

        :param incident_sub_type_id: The incident_sub_type_id of this IncidentSubTypeV2Do.
        :type incident_sub_type_id: str
        """
        self._incident_sub_type_id = incident_sub_type_id

    @property
    def incident_sub_type_name(self):
        """Gets the incident_sub_type_name of this IncidentSubTypeV2Do.

        工单子类型名称

        :return: The incident_sub_type_name of this IncidentSubTypeV2Do.
        :rtype: str
        """
        return self._incident_sub_type_name

    @incident_sub_type_name.setter
    def incident_sub_type_name(self, incident_sub_type_name):
        """Sets the incident_sub_type_name of this IncidentSubTypeV2Do.

        工单子类型名称

        :param incident_sub_type_name: The incident_sub_type_name of this IncidentSubTypeV2Do.
        :type incident_sub_type_name: str
        """
        self._incident_sub_type_name = incident_sub_type_name

    @property
    def incident_product_category_list(self):
        """Gets the incident_product_category_list of this IncidentSubTypeV2Do.

        产品类型列表

        :return: The incident_product_category_list of this IncidentSubTypeV2Do.
        :rtype: list[:class:`huaweicloudsdkosm.v2.IncidentProductCategoryV2`]
        """
        return self._incident_product_category_list

    @incident_product_category_list.setter
    def incident_product_category_list(self, incident_product_category_list):
        """Sets the incident_product_category_list of this IncidentSubTypeV2Do.

        产品类型列表

        :param incident_product_category_list: The incident_product_category_list of this IncidentSubTypeV2Do.
        :type incident_product_category_list: list[:class:`huaweicloudsdkosm.v2.IncidentProductCategoryV2`]
        """
        self._incident_product_category_list = incident_product_category_list

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
        if not isinstance(other, IncidentSubTypeV2Do):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
