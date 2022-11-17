# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_bucket_name': 'str',
        'x_namespace_name': 'str',
        'eihealth_project_id': 'str'
    }

    attribute_map = {
        'x_bucket_name': 'X-Bucket-Name',
        'x_namespace_name': 'X-Namespace-Name',
        'eihealth_project_id': 'eihealth_project_id'
    }

    def __init__(self, x_bucket_name=None, x_namespace_name=None, eihealth_project_id=None):
        """ShowProjectRequest

        The model defined in huaweicloud sdk

        :param x_bucket_name: X-Bucket-Name
        :type x_bucket_name: str
        :param x_namespace_name: X-Namespace
        :type x_namespace_name: str
        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        """
        
        

        self._x_bucket_name = None
        self._x_namespace_name = None
        self._eihealth_project_id = None
        self.discriminator = None

        if x_bucket_name is not None:
            self.x_bucket_name = x_bucket_name
        if x_namespace_name is not None:
            self.x_namespace_name = x_namespace_name
        self.eihealth_project_id = eihealth_project_id

    @property
    def x_bucket_name(self):
        """Gets the x_bucket_name of this ShowProjectRequest.

        X-Bucket-Name

        :return: The x_bucket_name of this ShowProjectRequest.
        :rtype: str
        """
        return self._x_bucket_name

    @x_bucket_name.setter
    def x_bucket_name(self, x_bucket_name):
        """Sets the x_bucket_name of this ShowProjectRequest.

        X-Bucket-Name

        :param x_bucket_name: The x_bucket_name of this ShowProjectRequest.
        :type x_bucket_name: str
        """
        self._x_bucket_name = x_bucket_name

    @property
    def x_namespace_name(self):
        """Gets the x_namespace_name of this ShowProjectRequest.

        X-Namespace

        :return: The x_namespace_name of this ShowProjectRequest.
        :rtype: str
        """
        return self._x_namespace_name

    @x_namespace_name.setter
    def x_namespace_name(self, x_namespace_name):
        """Sets the x_namespace_name of this ShowProjectRequest.

        X-Namespace

        :param x_namespace_name: The x_namespace_name of this ShowProjectRequest.
        :type x_namespace_name: str
        """
        self._x_namespace_name = x_namespace_name

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ShowProjectRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ShowProjectRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ShowProjectRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ShowProjectRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

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
        if not isinstance(other, ShowProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
