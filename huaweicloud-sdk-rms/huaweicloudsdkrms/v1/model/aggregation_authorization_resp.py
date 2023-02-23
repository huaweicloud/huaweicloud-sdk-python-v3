# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregationAuthorizationResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregation_authorization_urn': 'str',
        'authorized_account_id': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'aggregation_authorization_urn': 'aggregation_authorization_urn',
        'authorized_account_id': 'authorized_account_id',
        'created_at': 'created_at'
    }

    def __init__(self, aggregation_authorization_urn=None, authorized_account_id=None, created_at=None):
        """AggregationAuthorizationResp

        The model defined in huaweicloud sdk

        :param aggregation_authorization_urn: 资源聚合器授权标识符。
        :type aggregation_authorization_urn: str
        :param authorized_account_id: 授权的资源聚合器的帐号ID。
        :type authorized_account_id: str
        :param created_at: 资源聚合器授权的创建时间。
        :type created_at: str
        """
        
        

        self._aggregation_authorization_urn = None
        self._authorized_account_id = None
        self._created_at = None
        self.discriminator = None

        if aggregation_authorization_urn is not None:
            self.aggregation_authorization_urn = aggregation_authorization_urn
        if authorized_account_id is not None:
            self.authorized_account_id = authorized_account_id
        if created_at is not None:
            self.created_at = created_at

    @property
    def aggregation_authorization_urn(self):
        """Gets the aggregation_authorization_urn of this AggregationAuthorizationResp.

        资源聚合器授权标识符。

        :return: The aggregation_authorization_urn of this AggregationAuthorizationResp.
        :rtype: str
        """
        return self._aggregation_authorization_urn

    @aggregation_authorization_urn.setter
    def aggregation_authorization_urn(self, aggregation_authorization_urn):
        """Sets the aggregation_authorization_urn of this AggregationAuthorizationResp.

        资源聚合器授权标识符。

        :param aggregation_authorization_urn: The aggregation_authorization_urn of this AggregationAuthorizationResp.
        :type aggregation_authorization_urn: str
        """
        self._aggregation_authorization_urn = aggregation_authorization_urn

    @property
    def authorized_account_id(self):
        """Gets the authorized_account_id of this AggregationAuthorizationResp.

        授权的资源聚合器的帐号ID。

        :return: The authorized_account_id of this AggregationAuthorizationResp.
        :rtype: str
        """
        return self._authorized_account_id

    @authorized_account_id.setter
    def authorized_account_id(self, authorized_account_id):
        """Sets the authorized_account_id of this AggregationAuthorizationResp.

        授权的资源聚合器的帐号ID。

        :param authorized_account_id: The authorized_account_id of this AggregationAuthorizationResp.
        :type authorized_account_id: str
        """
        self._authorized_account_id = authorized_account_id

    @property
    def created_at(self):
        """Gets the created_at of this AggregationAuthorizationResp.

        资源聚合器授权的创建时间。

        :return: The created_at of this AggregationAuthorizationResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AggregationAuthorizationResp.

        资源聚合器授权的创建时间。

        :param created_at: The created_at of this AggregationAuthorizationResp.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, AggregationAuthorizationResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
