# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'parent_folder': 'str'
    }

    attribute_map = {
        'name': 'name',
        'parent_folder': 'parent_folder'
    }

    def __init__(self, name=None, parent_folder=None):
        r"""CreateDataReq

        The model defined in huaweicloud sdk

        :param name: 文件夹名称
        :type name: str
        :param parent_folder: 所在文件夹
        :type parent_folder: str
        """
        
        

        self._name = None
        self._parent_folder = None
        self.discriminator = None

        self.name = name
        if parent_folder is not None:
            self.parent_folder = parent_folder

    @property
    def name(self):
        r"""Gets the name of this CreateDataReq.

        文件夹名称

        :return: The name of this CreateDataReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDataReq.

        文件夹名称

        :param name: The name of this CreateDataReq.
        :type name: str
        """
        self._name = name

    @property
    def parent_folder(self):
        r"""Gets the parent_folder of this CreateDataReq.

        所在文件夹

        :return: The parent_folder of this CreateDataReq.
        :rtype: str
        """
        return self._parent_folder

    @parent_folder.setter
    def parent_folder(self, parent_folder):
        r"""Sets the parent_folder of this CreateDataReq.

        所在文件夹

        :param parent_folder: The parent_folder of this CreateDataReq.
        :type parent_folder: str
        """
        self._parent_folder = parent_folder

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
        if not isinstance(other, CreateDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
