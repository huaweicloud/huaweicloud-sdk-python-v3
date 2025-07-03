# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'launch_template_id': 'list[str]',
        'name': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'launch_template_id': 'launch_template_id',
        'name': 'name'
    }

    def __init__(self, limit=None, marker=None, launch_template_id=None, name=None):
        r"""ListTemplatesRequest

        The model defined in huaweicloud sdk

        :param limit: max number of resources to return
        :type limit: int
        :param marker: next page resource index id
        :type marker: str
        :param launch_template_id: 模板ID
        :type launch_template_id: list[str]
        :param name: 模板名称
        :type name: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._launch_template_id = None
        self._name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if launch_template_id is not None:
            self.launch_template_id = launch_template_id
        if name is not None:
            self.name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListTemplatesRequest.

        max number of resources to return

        :return: The limit of this ListTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTemplatesRequest.

        max number of resources to return

        :param limit: The limit of this ListTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListTemplatesRequest.

        next page resource index id

        :return: The marker of this ListTemplatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTemplatesRequest.

        next page resource index id

        :param marker: The marker of this ListTemplatesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def launch_template_id(self):
        r"""Gets the launch_template_id of this ListTemplatesRequest.

        模板ID

        :return: The launch_template_id of this ListTemplatesRequest.
        :rtype: list[str]
        """
        return self._launch_template_id

    @launch_template_id.setter
    def launch_template_id(self, launch_template_id):
        r"""Sets the launch_template_id of this ListTemplatesRequest.

        模板ID

        :param launch_template_id: The launch_template_id of this ListTemplatesRequest.
        :type launch_template_id: list[str]
        """
        self._launch_template_id = launch_template_id

    @property
    def name(self):
        r"""Gets the name of this ListTemplatesRequest.

        模板名称

        :return: The name of this ListTemplatesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTemplatesRequest.

        模板名称

        :param name: The name of this ListTemplatesRequest.
        :type name: list[str]
        """
        self._name = name

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
        if not isinstance(other, ListTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
