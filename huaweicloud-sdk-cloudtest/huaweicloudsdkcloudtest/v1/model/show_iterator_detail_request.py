# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIteratorDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iterator_id': 'str',
        'project_uuid': 'str'
    }

    attribute_map = {
        'iterator_id': 'iterator_id',
        'project_uuid': 'project_uuid'
    }

    def __init__(self, iterator_id=None, project_uuid=None):
        r"""ShowIteratorDetailRequest

        The model defined in huaweicloud sdk

        :param iterator_id: 迭代uri
        :type iterator_id: str
        :param project_uuid: 项目id
        :type project_uuid: str
        """
        
        

        self._iterator_id = None
        self._project_uuid = None
        self.discriminator = None

        self.iterator_id = iterator_id
        if project_uuid is not None:
            self.project_uuid = project_uuid

    @property
    def iterator_id(self):
        r"""Gets the iterator_id of this ShowIteratorDetailRequest.

        迭代uri

        :return: The iterator_id of this ShowIteratorDetailRequest.
        :rtype: str
        """
        return self._iterator_id

    @iterator_id.setter
    def iterator_id(self, iterator_id):
        r"""Sets the iterator_id of this ShowIteratorDetailRequest.

        迭代uri

        :param iterator_id: The iterator_id of this ShowIteratorDetailRequest.
        :type iterator_id: str
        """
        self._iterator_id = iterator_id

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ShowIteratorDetailRequest.

        项目id

        :return: The project_uuid of this ShowIteratorDetailRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ShowIteratorDetailRequest.

        项目id

        :param project_uuid: The project_uuid of this ShowIteratorDetailRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

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
        if not isinstance(other, ShowIteratorDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
