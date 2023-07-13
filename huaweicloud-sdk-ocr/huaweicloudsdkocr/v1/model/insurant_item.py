# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsurantItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'insurant_name': 'InsurancePolicyDetail',
        'insurant_sex': 'InsurancePolicyDetail',
        'insurant_birthday': 'InsurancePolicyDetail',
        'insurant_id_type': 'InsurancePolicyDetail',
        'insurant_id_number': 'InsurancePolicyDetail'
    }

    attribute_map = {
        'insurant_name': 'insurant_name',
        'insurant_sex': 'insurant_sex',
        'insurant_birthday': 'insurant_birthday',
        'insurant_id_type': 'insurant_id_type',
        'insurant_id_number': 'insurant_id_number'
    }

    def __init__(self, insurant_name=None, insurant_sex=None, insurant_birthday=None, insurant_id_type=None, insurant_id_number=None):
        """InsurantItem

        The model defined in huaweicloud sdk

        :param insurant_name: 
        :type insurant_name: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param insurant_sex: 
        :type insurant_sex: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param insurant_birthday: 
        :type insurant_birthday: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param insurant_id_type: 
        :type insurant_id_type: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param insurant_id_number: 
        :type insurant_id_number: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        
        

        self._insurant_name = None
        self._insurant_sex = None
        self._insurant_birthday = None
        self._insurant_id_type = None
        self._insurant_id_number = None
        self.discriminator = None

        if insurant_name is not None:
            self.insurant_name = insurant_name
        if insurant_sex is not None:
            self.insurant_sex = insurant_sex
        if insurant_birthday is not None:
            self.insurant_birthday = insurant_birthday
        if insurant_id_type is not None:
            self.insurant_id_type = insurant_id_type
        if insurant_id_number is not None:
            self.insurant_id_number = insurant_id_number

    @property
    def insurant_name(self):
        """Gets the insurant_name of this InsurantItem.

        :return: The insurant_name of this InsurantItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._insurant_name

    @insurant_name.setter
    def insurant_name(self, insurant_name):
        """Sets the insurant_name of this InsurantItem.

        :param insurant_name: The insurant_name of this InsurantItem.
        :type insurant_name: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._insurant_name = insurant_name

    @property
    def insurant_sex(self):
        """Gets the insurant_sex of this InsurantItem.

        :return: The insurant_sex of this InsurantItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._insurant_sex

    @insurant_sex.setter
    def insurant_sex(self, insurant_sex):
        """Sets the insurant_sex of this InsurantItem.

        :param insurant_sex: The insurant_sex of this InsurantItem.
        :type insurant_sex: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._insurant_sex = insurant_sex

    @property
    def insurant_birthday(self):
        """Gets the insurant_birthday of this InsurantItem.

        :return: The insurant_birthday of this InsurantItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._insurant_birthday

    @insurant_birthday.setter
    def insurant_birthday(self, insurant_birthday):
        """Sets the insurant_birthday of this InsurantItem.

        :param insurant_birthday: The insurant_birthday of this InsurantItem.
        :type insurant_birthday: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._insurant_birthday = insurant_birthday

    @property
    def insurant_id_type(self):
        """Gets the insurant_id_type of this InsurantItem.

        :return: The insurant_id_type of this InsurantItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._insurant_id_type

    @insurant_id_type.setter
    def insurant_id_type(self, insurant_id_type):
        """Sets the insurant_id_type of this InsurantItem.

        :param insurant_id_type: The insurant_id_type of this InsurantItem.
        :type insurant_id_type: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._insurant_id_type = insurant_id_type

    @property
    def insurant_id_number(self):
        """Gets the insurant_id_number of this InsurantItem.

        :return: The insurant_id_number of this InsurantItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._insurant_id_number

    @insurant_id_number.setter
    def insurant_id_number(self, insurant_id_number):
        """Sets the insurant_id_number of this InsurantItem.

        :param insurant_id_number: The insurant_id_number of this InsurantItem.
        :type insurant_id_number: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._insurant_id_number = insurant_id_number

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
        if not isinstance(other, InsurantItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
