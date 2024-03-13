# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalEipRequestBody:

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
        'global_eip': 'CreateGlobalEipRequestBodyGlobalEip'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'global_eip': 'global_eip'
    }

    def __init__(self, dry_run=None, global_eip=None):
        """CreateGlobalEipRequestBody

        The model defined in huaweicloud sdk

        :param dry_run: 
        :type dry_run: bool
        :param global_eip: 
        :type global_eip: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEip`
        """
        
        

        self._dry_run = None
        self._global_eip = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.global_eip = global_eip

    @property
    def dry_run(self):
        """Gets the dry_run of this CreateGlobalEipRequestBody.

        :return: The dry_run of this CreateGlobalEipRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreateGlobalEipRequestBody.

        :param dry_run: The dry_run of this CreateGlobalEipRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def global_eip(self):
        """Gets the global_eip of this CreateGlobalEipRequestBody.

        :return: The global_eip of this CreateGlobalEipRequestBody.
        :rtype: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEip`
        """
        return self._global_eip

    @global_eip.setter
    def global_eip(self, global_eip):
        """Sets the global_eip of this CreateGlobalEipRequestBody.

        :param global_eip: The global_eip of this CreateGlobalEipRequestBody.
        :type global_eip: :class:`huaweicloudsdkgeip.v3.CreateGlobalEipRequestBodyGlobalEip`
        """
        self._global_eip = global_eip

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
        if not isinstance(other, CreateGlobalEipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
