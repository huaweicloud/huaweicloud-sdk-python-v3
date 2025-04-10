# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGdgwRoutetableRequestBody:

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
        'gdgw_routetable': 'GdgwRouteTableRequest'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'gdgw_routetable': 'gdgw_routetable'
    }

    def __init__(self, dry_run=None, gdgw_routetable=None):
        r"""UpdateGdgwRoutetableRequestBody

        The model defined in huaweicloud sdk

        :param dry_run: 是否dry run模式执行
        :type dry_run: bool
        :param gdgw_routetable: 
        :type gdgw_routetable: :class:`huaweicloudsdkdc.v3.GdgwRouteTableRequest`
        """
        
        

        self._dry_run = None
        self._gdgw_routetable = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        if gdgw_routetable is not None:
            self.gdgw_routetable = gdgw_routetable

    @property
    def dry_run(self):
        r"""Gets the dry_run of this UpdateGdgwRoutetableRequestBody.

        是否dry run模式执行

        :return: The dry_run of this UpdateGdgwRoutetableRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this UpdateGdgwRoutetableRequestBody.

        是否dry run模式执行

        :param dry_run: The dry_run of this UpdateGdgwRoutetableRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def gdgw_routetable(self):
        r"""Gets the gdgw_routetable of this UpdateGdgwRoutetableRequestBody.

        :return: The gdgw_routetable of this UpdateGdgwRoutetableRequestBody.
        :rtype: :class:`huaweicloudsdkdc.v3.GdgwRouteTableRequest`
        """
        return self._gdgw_routetable

    @gdgw_routetable.setter
    def gdgw_routetable(self, gdgw_routetable):
        r"""Sets the gdgw_routetable of this UpdateGdgwRoutetableRequestBody.

        :param gdgw_routetable: The gdgw_routetable of this UpdateGdgwRoutetableRequestBody.
        :type gdgw_routetable: :class:`huaweicloudsdkdc.v3.GdgwRouteTableRequest`
        """
        self._gdgw_routetable = gdgw_routetable

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
        if not isinstance(other, UpdateGdgwRoutetableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
