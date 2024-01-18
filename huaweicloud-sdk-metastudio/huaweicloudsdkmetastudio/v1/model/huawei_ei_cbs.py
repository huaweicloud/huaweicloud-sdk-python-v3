# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HuaweiEiCbs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'region': 'int',
        'cbs_project_id': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'region': 'region',
        'cbs_project_id': 'cbs_project_id'
    }

    def __init__(self, app_id=None, region=None, cbs_project_id=None):
        """HuaweiEiCbs

        The model defined in huaweicloud sdk

        :param app_id: CBS应用ID。
        :type app_id: str
        :param region: CBS所在区域
        :type region: int
        :param cbs_project_id: CBS所在区域的projectId
        :type cbs_project_id: str
        """
        
        

        self._app_id = None
        self._region = None
        self._cbs_project_id = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if region is not None:
            self.region = region
        if cbs_project_id is not None:
            self.cbs_project_id = cbs_project_id

    @property
    def app_id(self):
        """Gets the app_id of this HuaweiEiCbs.

        CBS应用ID。

        :return: The app_id of this HuaweiEiCbs.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this HuaweiEiCbs.

        CBS应用ID。

        :param app_id: The app_id of this HuaweiEiCbs.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def region(self):
        """Gets the region of this HuaweiEiCbs.

        CBS所在区域

        :return: The region of this HuaweiEiCbs.
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this HuaweiEiCbs.

        CBS所在区域

        :param region: The region of this HuaweiEiCbs.
        :type region: int
        """
        self._region = region

    @property
    def cbs_project_id(self):
        """Gets the cbs_project_id of this HuaweiEiCbs.

        CBS所在区域的projectId

        :return: The cbs_project_id of this HuaweiEiCbs.
        :rtype: str
        """
        return self._cbs_project_id

    @cbs_project_id.setter
    def cbs_project_id(self, cbs_project_id):
        """Sets the cbs_project_id of this HuaweiEiCbs.

        CBS所在区域的projectId

        :param cbs_project_id: The cbs_project_id of this HuaweiEiCbs.
        :type cbs_project_id: str
        """
        self._cbs_project_id = cbs_project_id

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
        if not isinstance(other, HuaweiEiCbs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
