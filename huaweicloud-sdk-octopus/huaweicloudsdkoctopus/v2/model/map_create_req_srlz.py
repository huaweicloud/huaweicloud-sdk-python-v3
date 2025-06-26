# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MapCreateReqSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'FileCreateReqSrlz',
        'version': 'MapVersionEnum',
        'agreement_confirm': 'bool'
    }

    attribute_map = {
        'file': 'file',
        'version': 'version',
        'agreement_confirm': 'agreement_confirm'
    }

    def __init__(self, file=None, version=None, agreement_confirm=None):
        r"""MapCreateReqSrlz

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateReqSrlz`
        :param version: 
        :type version: :class:`huaweicloudsdkoctopus.v2.MapVersionEnum`
        :param agreement_confirm: 是否同意协议，必须为true
        :type agreement_confirm: bool
        """
        
        

        self._file = None
        self._version = None
        self._agreement_confirm = None
        self.discriminator = None

        self.file = file
        self.version = version
        self.agreement_confirm = agreement_confirm

    @property
    def file(self):
        r"""Gets the file of this MapCreateReqSrlz.

        :return: The file of this MapCreateReqSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.FileCreateReqSrlz`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this MapCreateReqSrlz.

        :param file: The file of this MapCreateReqSrlz.
        :type file: :class:`huaweicloudsdkoctopus.v2.FileCreateReqSrlz`
        """
        self._file = file

    @property
    def version(self):
        r"""Gets the version of this MapCreateReqSrlz.

        :return: The version of this MapCreateReqSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.MapVersionEnum`
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this MapCreateReqSrlz.

        :param version: The version of this MapCreateReqSrlz.
        :type version: :class:`huaweicloudsdkoctopus.v2.MapVersionEnum`
        """
        self._version = version

    @property
    def agreement_confirm(self):
        r"""Gets the agreement_confirm of this MapCreateReqSrlz.

        是否同意协议，必须为true

        :return: The agreement_confirm of this MapCreateReqSrlz.
        :rtype: bool
        """
        return self._agreement_confirm

    @agreement_confirm.setter
    def agreement_confirm(self, agreement_confirm):
        r"""Sets the agreement_confirm of this MapCreateReqSrlz.

        是否同意协议，必须为true

        :param agreement_confirm: The agreement_confirm of this MapCreateReqSrlz.
        :type agreement_confirm: bool
        """
        self._agreement_confirm = agreement_confirm

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
        if not isinstance(other, MapCreateReqSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
