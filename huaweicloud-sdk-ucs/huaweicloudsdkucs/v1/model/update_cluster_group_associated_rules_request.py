# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClusterGroupAssociatedRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clustergroupid': 'str',
        'body': 'UpdateAssociatedRulesRequest'
    }

    attribute_map = {
        'clustergroupid': 'clustergroupid',
        'body': 'body'
    }

    def __init__(self, clustergroupid=None, body=None):
        r"""UpdateClusterGroupAssociatedRulesRequest

        The model defined in huaweicloud sdk

        :param clustergroupid: 容器舰队ID
        :type clustergroupid: str
        :param body: Body of the UpdateClusterGroupAssociatedRulesRequest
        :type body: :class:`huaweicloudsdkucs.v1.UpdateAssociatedRulesRequest`
        """
        
        

        self._clustergroupid = None
        self._body = None
        self.discriminator = None

        self.clustergroupid = clustergroupid
        if body is not None:
            self.body = body

    @property
    def clustergroupid(self):
        r"""Gets the clustergroupid of this UpdateClusterGroupAssociatedRulesRequest.

        容器舰队ID

        :return: The clustergroupid of this UpdateClusterGroupAssociatedRulesRequest.
        :rtype: str
        """
        return self._clustergroupid

    @clustergroupid.setter
    def clustergroupid(self, clustergroupid):
        r"""Sets the clustergroupid of this UpdateClusterGroupAssociatedRulesRequest.

        容器舰队ID

        :param clustergroupid: The clustergroupid of this UpdateClusterGroupAssociatedRulesRequest.
        :type clustergroupid: str
        """
        self._clustergroupid = clustergroupid

    @property
    def body(self):
        r"""Gets the body of this UpdateClusterGroupAssociatedRulesRequest.

        :return: The body of this UpdateClusterGroupAssociatedRulesRequest.
        :rtype: :class:`huaweicloudsdkucs.v1.UpdateAssociatedRulesRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateClusterGroupAssociatedRulesRequest.

        :param body: The body of this UpdateClusterGroupAssociatedRulesRequest.
        :type body: :class:`huaweicloudsdkucs.v1.UpdateAssociatedRulesRequest`
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
        if not isinstance(other, UpdateClusterGroupAssociatedRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
