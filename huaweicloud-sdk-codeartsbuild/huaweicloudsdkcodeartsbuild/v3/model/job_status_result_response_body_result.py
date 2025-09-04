# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobStatusResultResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'building': 'bool',
        'build_result': 'str',
        'region': 'str'
    }

    attribute_map = {
        'building': 'building',
        'build_result': 'build_result',
        'region': 'region'
    }

    def __init__(self, building=None, build_result=None, region=None):
        r"""JobStatusResultResponseBodyResult

        The model defined in huaweicloud sdk

        :param building: 是否构建中
        :type building: bool
        :param build_result: 构建结果
        :type build_result: str
        :param region: region
        :type region: str
        """
        
        

        self._building = None
        self._build_result = None
        self._region = None
        self.discriminator = None

        if building is not None:
            self.building = building
        if build_result is not None:
            self.build_result = build_result
        if region is not None:
            self.region = region

    @property
    def building(self):
        r"""Gets the building of this JobStatusResultResponseBodyResult.

        是否构建中

        :return: The building of this JobStatusResultResponseBodyResult.
        :rtype: bool
        """
        return self._building

    @building.setter
    def building(self, building):
        r"""Sets the building of this JobStatusResultResponseBodyResult.

        是否构建中

        :param building: The building of this JobStatusResultResponseBodyResult.
        :type building: bool
        """
        self._building = building

    @property
    def build_result(self):
        r"""Gets the build_result of this JobStatusResultResponseBodyResult.

        构建结果

        :return: The build_result of this JobStatusResultResponseBodyResult.
        :rtype: str
        """
        return self._build_result

    @build_result.setter
    def build_result(self, build_result):
        r"""Sets the build_result of this JobStatusResultResponseBodyResult.

        构建结果

        :param build_result: The build_result of this JobStatusResultResponseBodyResult.
        :type build_result: str
        """
        self._build_result = build_result

    @property
    def region(self):
        r"""Gets the region of this JobStatusResultResponseBodyResult.

        region

        :return: The region of this JobStatusResultResponseBodyResult.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this JobStatusResultResponseBodyResult.

        region

        :param region: The region of this JobStatusResultResponseBodyResult.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, JobStatusResultResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
