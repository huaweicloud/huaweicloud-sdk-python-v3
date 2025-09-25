# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateYmlsReqEdit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'modify': 'UpdateYmlsReqEditModify',
        'delete': 'UpdateYmlsReqEditModify',
        'reset': 'UpdateYmlsReqEditModify'
    }

    attribute_map = {
        'modify': 'modify',
        'delete': 'delete',
        'reset': 'reset'
    }

    def __init__(self, modify=None, delete=None, reset=None):
        r"""UpdateYmlsReqEdit

        The model defined in huaweicloud sdk

        :param modify: 
        :type modify: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        :param delete: 
        :type delete: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        :param reset: 
        :type reset: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        
        

        self._modify = None
        self._delete = None
        self._reset = None
        self.discriminator = None

        if modify is not None:
            self.modify = modify
        if delete is not None:
            self.delete = delete
        if reset is not None:
            self.reset = reset

    @property
    def modify(self):
        r"""Gets the modify of this UpdateYmlsReqEdit.

        :return: The modify of this UpdateYmlsReqEdit.
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        return self._modify

    @modify.setter
    def modify(self, modify):
        r"""Sets the modify of this UpdateYmlsReqEdit.

        :param modify: The modify of this UpdateYmlsReqEdit.
        :type modify: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        self._modify = modify

    @property
    def delete(self):
        r"""Gets the delete of this UpdateYmlsReqEdit.

        :return: The delete of this UpdateYmlsReqEdit.
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this UpdateYmlsReqEdit.

        :param delete: The delete of this UpdateYmlsReqEdit.
        :type delete: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        self._delete = delete

    @property
    def reset(self):
        r"""Gets the reset of this UpdateYmlsReqEdit.

        :return: The reset of this UpdateYmlsReqEdit.
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        return self._reset

    @reset.setter
    def reset(self, reset):
        r"""Sets the reset of this UpdateYmlsReqEdit.

        :param reset: The reset of this UpdateYmlsReqEdit.
        :type reset: :class:`huaweicloudsdkcss.v1.UpdateYmlsReqEditModify`
        """
        self._reset = reset

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
        if not isinstance(other, UpdateYmlsReqEdit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
