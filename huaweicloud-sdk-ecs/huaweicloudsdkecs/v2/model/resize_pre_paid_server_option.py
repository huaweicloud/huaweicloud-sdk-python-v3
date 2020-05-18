# coding: utf-8

import pprint
import re

import six


class ResizePrePaidServerOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'flavor_ref': 'str',
        'dedicated_host_id': 'str',
        'extendparam': 'ResizeServerExtendParam'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'dedicated_host_id': 'dedicated_host_id',
        'extendparam': 'extendparam'
    }

    def __init__(self, flavor_ref=None, dedicated_host_id=None, extendparam=None):  # noqa: E501
        """ResizePrePaidServerOption - a model defined in huaweicloud sdk"""

        self._flavor_ref = None
        self._dedicated_host_id = None
        self._extendparam = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if extendparam is not None:
            self.extendparam = extendparam

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this ResizePrePaidServerOption.

        变更后的云服务器规格ID。

        :return: The flavor_ref of this ResizePrePaidServerOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this ResizePrePaidServerOption.

        变更后的云服务器规格ID。

        :param flavor_ref: The flavor_ref of this ResizePrePaidServerOption.
        :type: str
        """
        self._flavor_ref = flavor_ref

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this ResizePrePaidServerOption.

        新专属主机ID（仅适用于专属主机上的弹性云服务器）。

        :return: The dedicated_host_id of this ResizePrePaidServerOption.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this ResizePrePaidServerOption.

        新专属主机ID（仅适用于专属主机上的弹性云服务器）。

        :param dedicated_host_id: The dedicated_host_id of this ResizePrePaidServerOption.
        :type: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def extendparam(self):
        """Gets the extendparam of this ResizePrePaidServerOption.


        :return: The extendparam of this ResizePrePaidServerOption.
        :rtype: ResizeServerExtendParam
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this ResizePrePaidServerOption.


        :param extendparam: The extendparam of this ResizePrePaidServerOption.
        :type: ResizeServerExtendParam
        """
        self._extendparam = extendparam

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResizePrePaidServerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
