# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDrRelationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_dr_relations': 'list[InstanceDrRelation]'
    }

    attribute_map = {
        'instance_dr_relations': 'instance_dr_relations'
    }

    def __init__(self, instance_dr_relations=None):
        r"""ListDrRelationsResponse

        The model defined in huaweicloud sdk

        :param instance_dr_relations: 
        :type instance_dr_relations: list[:class:`huaweicloudsdkrds.v3.InstanceDrRelation`]
        """
        
        super(ListDrRelationsResponse, self).__init__()

        self._instance_dr_relations = None
        self.discriminator = None

        if instance_dr_relations is not None:
            self.instance_dr_relations = instance_dr_relations

    @property
    def instance_dr_relations(self):
        r"""Gets the instance_dr_relations of this ListDrRelationsResponse.

        :return: The instance_dr_relations of this ListDrRelationsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.InstanceDrRelation`]
        """
        return self._instance_dr_relations

    @instance_dr_relations.setter
    def instance_dr_relations(self, instance_dr_relations):
        r"""Sets the instance_dr_relations of this ListDrRelationsResponse.

        :param instance_dr_relations: The instance_dr_relations of this ListDrRelationsResponse.
        :type instance_dr_relations: list[:class:`huaweicloudsdkrds.v3.InstanceDrRelation`]
        """
        self._instance_dr_relations = instance_dr_relations

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
        if not isinstance(other, ListDrRelationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
