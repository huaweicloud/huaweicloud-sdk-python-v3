# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateGlobalEipRequestBody:

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
        'global_eip': 'BatchCreateGlobalEipRequestBodyGlobalEip'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'global_eip': 'global_eip'
    }

    def __init__(self, dry_run=None, global_eip=None):
        r"""BatchCreateGlobalEipRequestBody

        The model defined in huaweicloud sdk

        :param dry_run: 
        :type dry_run: bool
        :param global_eip: 
        :type global_eip: :class:`huaweicloudsdkgeip.v3.BatchCreateGlobalEipRequestBodyGlobalEip`
        """
        
        

        self._dry_run = None
        self._global_eip = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.global_eip = global_eip

    @property
    def dry_run(self):
        r"""Gets the dry_run of this BatchCreateGlobalEipRequestBody.

        :return: The dry_run of this BatchCreateGlobalEipRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this BatchCreateGlobalEipRequestBody.

        :param dry_run: The dry_run of this BatchCreateGlobalEipRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def global_eip(self):
        r"""Gets the global_eip of this BatchCreateGlobalEipRequestBody.

        :return: The global_eip of this BatchCreateGlobalEipRequestBody.
        :rtype: :class:`huaweicloudsdkgeip.v3.BatchCreateGlobalEipRequestBodyGlobalEip`
        """
        return self._global_eip

    @global_eip.setter
    def global_eip(self, global_eip):
        r"""Sets the global_eip of this BatchCreateGlobalEipRequestBody.

        :param global_eip: The global_eip of this BatchCreateGlobalEipRequestBody.
        :type global_eip: :class:`huaweicloudsdkgeip.v3.BatchCreateGlobalEipRequestBodyGlobalEip`
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
        if not isinstance(other, BatchCreateGlobalEipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
