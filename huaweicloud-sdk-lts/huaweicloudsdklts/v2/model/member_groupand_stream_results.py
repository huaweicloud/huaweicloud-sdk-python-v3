# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberGroupandStreamResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_group_name': 'str',
        'log_streams': 'list[MemberGroupandStreamLogStreams]'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'log_streams': 'log_streams'
    }

    def __init__(self, log_group_id=None, log_group_name=None, log_streams=None):
        r"""MemberGroupandStreamResults

        The model defined in huaweicloud sdk

        :param log_group_id: 
        :type log_group_id: str
        :param log_group_name: 
        :type log_group_name: str
        :param log_streams: 
        :type log_streams: list[:class:`huaweicloudsdklts.v2.MemberGroupandStreamLogStreams`]
        """
        
        

        self._log_group_id = None
        self._log_group_name = None
        self._log_streams = None
        self.discriminator = None

        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_streams is not None:
            self.log_streams = log_streams

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this MemberGroupandStreamResults.

        :return: The log_group_id of this MemberGroupandStreamResults.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this MemberGroupandStreamResults.

        :param log_group_id: The log_group_id of this MemberGroupandStreamResults.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this MemberGroupandStreamResults.

        :return: The log_group_name of this MemberGroupandStreamResults.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this MemberGroupandStreamResults.

        :param log_group_name: The log_group_name of this MemberGroupandStreamResults.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_streams(self):
        r"""Gets the log_streams of this MemberGroupandStreamResults.

        :return: The log_streams of this MemberGroupandStreamResults.
        :rtype: list[:class:`huaweicloudsdklts.v2.MemberGroupandStreamLogStreams`]
        """
        return self._log_streams

    @log_streams.setter
    def log_streams(self, log_streams):
        r"""Sets the log_streams of this MemberGroupandStreamResults.

        :param log_streams: The log_streams of this MemberGroupandStreamResults.
        :type log_streams: list[:class:`huaweicloudsdklts.v2.MemberGroupandStreamLogStreams`]
        """
        self._log_streams = log_streams

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
        if not isinstance(other, MemberGroupandStreamResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
