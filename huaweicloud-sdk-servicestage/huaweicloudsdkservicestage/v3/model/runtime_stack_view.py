# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeStackView:

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
        'deploy_mode': 'str',
        'version': 'str',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'deploy_mode': 'deploy_mode',
        'version': 'version',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, name=None, deploy_mode=None, version=None, type=None, status=None):
        r"""RuntimeStackView

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param deploy_mode: 
        :type deploy_mode: str
        :param version: 
        :type version: str
        :param type: 
        :type type: str
        :param status: 
        :type status: str
        """
        
        

        self._name = None
        self._deploy_mode = None
        self._version = None
        self._type = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        if version is not None:
            self.version = version
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status

    @property
    def name(self):
        r"""Gets the name of this RuntimeStackView.

        :return: The name of this RuntimeStackView.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuntimeStackView.

        :param name: The name of this RuntimeStackView.
        :type name: str
        """
        self._name = name

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this RuntimeStackView.

        :return: The deploy_mode of this RuntimeStackView.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this RuntimeStackView.

        :param deploy_mode: The deploy_mode of this RuntimeStackView.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def version(self):
        r"""Gets the version of this RuntimeStackView.

        :return: The version of this RuntimeStackView.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this RuntimeStackView.

        :param version: The version of this RuntimeStackView.
        :type version: str
        """
        self._version = version

    @property
    def type(self):
        r"""Gets the type of this RuntimeStackView.

        :return: The type of this RuntimeStackView.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuntimeStackView.

        :param type: The type of this RuntimeStackView.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this RuntimeStackView.

        :return: The status of this RuntimeStackView.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RuntimeStackView.

        :param status: The status of this RuntimeStackView.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, RuntimeStackView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
