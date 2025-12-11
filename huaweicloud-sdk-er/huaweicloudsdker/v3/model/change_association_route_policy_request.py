# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeAssociationRoutePolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'route_table_id': 'str',
        'association_id': 'str',
        'body': 'AssociationRoutePolicyRequestBody'
    }

    attribute_map = {
        'er_id': 'er_id',
        'route_table_id': 'route_table_id',
        'association_id': 'association_id',
        'body': 'body'
    }

    def __init__(self, er_id=None, route_table_id=None, association_id=None, body=None):
        r"""ChangeAssociationRoutePolicyRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param route_table_id: 路由表ID
        :type route_table_id: str
        :param association_id: 关联ID
        :type association_id: str
        :param body: Body of the ChangeAssociationRoutePolicyRequest
        :type body: :class:`huaweicloudsdker.v3.AssociationRoutePolicyRequestBody`
        """
        
        

        self._er_id = None
        self._route_table_id = None
        self._association_id = None
        self._body = None
        self.discriminator = None

        self.er_id = er_id
        self.route_table_id = route_table_id
        self.association_id = association_id
        if body is not None:
            self.body = body

    @property
    def er_id(self):
        r"""Gets the er_id of this ChangeAssociationRoutePolicyRequest.

        企业路由器实例ID

        :return: The er_id of this ChangeAssociationRoutePolicyRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this ChangeAssociationRoutePolicyRequest.

        企业路由器实例ID

        :param er_id: The er_id of this ChangeAssociationRoutePolicyRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def route_table_id(self):
        r"""Gets the route_table_id of this ChangeAssociationRoutePolicyRequest.

        路由表ID

        :return: The route_table_id of this ChangeAssociationRoutePolicyRequest.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        r"""Sets the route_table_id of this ChangeAssociationRoutePolicyRequest.

        路由表ID

        :param route_table_id: The route_table_id of this ChangeAssociationRoutePolicyRequest.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def association_id(self):
        r"""Gets the association_id of this ChangeAssociationRoutePolicyRequest.

        关联ID

        :return: The association_id of this ChangeAssociationRoutePolicyRequest.
        :rtype: str
        """
        return self._association_id

    @association_id.setter
    def association_id(self, association_id):
        r"""Sets the association_id of this ChangeAssociationRoutePolicyRequest.

        关联ID

        :param association_id: The association_id of this ChangeAssociationRoutePolicyRequest.
        :type association_id: str
        """
        self._association_id = association_id

    @property
    def body(self):
        r"""Gets the body of this ChangeAssociationRoutePolicyRequest.

        :return: The body of this ChangeAssociationRoutePolicyRequest.
        :rtype: :class:`huaweicloudsdker.v3.AssociationRoutePolicyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ChangeAssociationRoutePolicyRequest.

        :param body: The body of this ChangeAssociationRoutePolicyRequest.
        :type body: :class:`huaweicloudsdker.v3.AssociationRoutePolicyRequestBody`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangeAssociationRoutePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
