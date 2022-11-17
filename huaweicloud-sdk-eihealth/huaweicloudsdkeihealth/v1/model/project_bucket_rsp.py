# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectBucketRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'eihealth_project_name': 'str',
        'type': 'str',
        'quote_root': 'bool'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'eihealth_project_name': 'eihealth_project_name',
        'type': 'type',
        'quote_root': 'quote_root'
    }

    def __init__(self, eihealth_project_id=None, eihealth_project_name=None, type=None, quote_root=None):
        """ProjectBucketRsp

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 项目编号
        :type eihealth_project_id: str
        :param eihealth_project_name: 项目名称
        :type eihealth_project_name: str
        :param type: 桶类型(real:项目桶,quote:引用桶)
        :type type: str
        :param quote_root: 是否引用桶根路径
        :type quote_root: bool
        """
        
        

        self._eihealth_project_id = None
        self._eihealth_project_name = None
        self._type = None
        self._quote_root = None
        self.discriminator = None

        if eihealth_project_id is not None:
            self.eihealth_project_id = eihealth_project_id
        if eihealth_project_name is not None:
            self.eihealth_project_name = eihealth_project_name
        if type is not None:
            self.type = type
        if quote_root is not None:
            self.quote_root = quote_root

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ProjectBucketRsp.

        项目编号

        :return: The eihealth_project_id of this ProjectBucketRsp.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ProjectBucketRsp.

        项目编号

        :param eihealth_project_id: The eihealth_project_id of this ProjectBucketRsp.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def eihealth_project_name(self):
        """Gets the eihealth_project_name of this ProjectBucketRsp.

        项目名称

        :return: The eihealth_project_name of this ProjectBucketRsp.
        :rtype: str
        """
        return self._eihealth_project_name

    @eihealth_project_name.setter
    def eihealth_project_name(self, eihealth_project_name):
        """Sets the eihealth_project_name of this ProjectBucketRsp.

        项目名称

        :param eihealth_project_name: The eihealth_project_name of this ProjectBucketRsp.
        :type eihealth_project_name: str
        """
        self._eihealth_project_name = eihealth_project_name

    @property
    def type(self):
        """Gets the type of this ProjectBucketRsp.

        桶类型(real:项目桶,quote:引用桶)

        :return: The type of this ProjectBucketRsp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProjectBucketRsp.

        桶类型(real:项目桶,quote:引用桶)

        :param type: The type of this ProjectBucketRsp.
        :type type: str
        """
        self._type = type

    @property
    def quote_root(self):
        """Gets the quote_root of this ProjectBucketRsp.

        是否引用桶根路径

        :return: The quote_root of this ProjectBucketRsp.
        :rtype: bool
        """
        return self._quote_root

    @quote_root.setter
    def quote_root(self, quote_root):
        """Sets the quote_root of this ProjectBucketRsp.

        是否引用桶根路径

        :param quote_root: The quote_root of this ProjectBucketRsp.
        :type quote_root: bool
        """
        self._quote_root = quote_root

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
        if not isinstance(other, ProjectBucketRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
