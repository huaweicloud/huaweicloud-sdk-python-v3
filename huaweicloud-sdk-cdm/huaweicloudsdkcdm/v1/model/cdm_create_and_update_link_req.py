# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmCreateAndUpdateLinkReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links': 'list[Links]'
    }

    attribute_map = {
        'links': 'links'
    }

    def __init__(self, links=None):
        """CdmCreateAndUpdateLinkReq

        The model defined in huaweicloud sdk

        :param links: 连接列表，请参见links数据结构说明
        :type links: list[:class:`huaweicloudsdkcdm.v1.Links`]
        """
        
        

        self._links = None
        self.discriminator = None

        self.links = links

    @property
    def links(self):
        """Gets the links of this CdmCreateAndUpdateLinkReq.

        连接列表，请参见links数据结构说明

        :return: The links of this CdmCreateAndUpdateLinkReq.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CdmCreateAndUpdateLinkReq.

        连接列表，请参见links数据结构说明

        :param links: The links of this CdmCreateAndUpdateLinkReq.
        :type links: list[:class:`huaweicloudsdkcdm.v1.Links`]
        """
        self._links = links

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
        if not isinstance(other, CdmCreateAndUpdateLinkReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
