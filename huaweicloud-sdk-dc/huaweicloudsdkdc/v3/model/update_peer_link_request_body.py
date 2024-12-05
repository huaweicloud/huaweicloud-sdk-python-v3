# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePeerLinkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'peer_link': 'UpdatePeerLinkRequestBodyPeerLink'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'peer_link': 'peer_link'
    }

    def __init__(self, dry_run=None, peer_link=None):
        """UpdatePeerLinkRequestBody

        The model defined in huaweicloud sdk

        :param dry_run: 空运行 - true 是 - false 否
        :type dry_run: bool
        :param peer_link: 
        :type peer_link: :class:`huaweicloudsdkdc.v3.UpdatePeerLinkRequestBodyPeerLink`
        """
        
        

        self._dry_run = None
        self._peer_link = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        if peer_link is not None:
            self.peer_link = peer_link

    @property
    def dry_run(self):
        """Gets the dry_run of this UpdatePeerLinkRequestBody.

        空运行 - true 是 - false 否

        :return: The dry_run of this UpdatePeerLinkRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this UpdatePeerLinkRequestBody.

        空运行 - true 是 - false 否

        :param dry_run: The dry_run of this UpdatePeerLinkRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def peer_link(self):
        """Gets the peer_link of this UpdatePeerLinkRequestBody.

        :return: The peer_link of this UpdatePeerLinkRequestBody.
        :rtype: :class:`huaweicloudsdkdc.v3.UpdatePeerLinkRequestBodyPeerLink`
        """
        return self._peer_link

    @peer_link.setter
    def peer_link(self, peer_link):
        """Sets the peer_link of this UpdatePeerLinkRequestBody.

        :param peer_link: The peer_link of this UpdatePeerLinkRequestBody.
        :type peer_link: :class:`huaweicloudsdkdc.v3.UpdatePeerLinkRequestBodyPeerLink`
        """
        self._peer_link = peer_link

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
        if not isinstance(other, UpdatePeerLinkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
